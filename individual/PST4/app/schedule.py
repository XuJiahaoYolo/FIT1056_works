import json
# from app.student import StudentUser  # Assuming StudentUser is defined in app.student
# Corrected: TeacherUser and Course now come from the same file.
from app.teacher import TeacherUser, Course
from app.student import StudentUser  # Import StudentUser from student module

class ScheduleManager:
    """The main controller for all business logic and data handling."""

    def __init__(self, data_path="data/msms.json"):
        self.data_path = data_path
        self.students = []
        self.teachers = []
        self.courses = []
        self.next_lesson_id = 1
        self._load_data()

    def _load_data(self):
        """Loads data from the JSON file and populates the object lists."""
        try:
            with open(self.data_path, 'r') as f:
                data = json.load(f)
                # The logic here remains the same, but the source of the Course class has changed.
                # TODO: For each dictionary in data['students'], create a StudentUser object and append to self.students.
                student_dicts = data.get('students', [])
                for s_dict in student_dicts:
                    student = StudentUser(
                        s_dict.get('id'),
                        s_dict.get('name'),
                        s_dict.get('instrument')
                    )
                    self.students.append(student)
                # TODO: Do the same for teachers (creating TeacherUser objects).
                teacher_dicts = data.get('teachers', [])
                for t_dict in teacher_dicts:
                    teacher = TeacherUser(
                        t_dict.get('id'),
                        t_dict.get('name'),
                        t_dict.get('specialization')
                    )
                    self.teachers.append(teacher)
                # TODO: Do the same for courses (creating Course objects).
                course_dicts = data.get('courses', [])
                for c_dict in course_dicts:
                    course = Course(
                        c_dict.get('id'),
                        c_dict.get('name'),
                        c_dict.get('instrument'),
                        c_dict.get('teacher_id'),
                        c_dict.get('weekday'),
                        c_dict.get('enrolled_student_ids', [])
                    )
                    if 'check_ins' in c_dict:
                        course.check_ins = c_dict['check_ins']
                    self.courses.append(course)
                if self.courses:
                    max_lesson_id = max(int(c.id.split('L')[-1]) for c in self.courses)
                    self.next_lesson_id = max_lesson_id + 1
        except FileNotFoundError:
            print("Data file not found. Starting with a clean state.")
        except Exception as e:
            print(f"An error occurred during data loading: {e}")

    def _save_data(self):
        """Converts object lists back to dictionaries and saves to JSON."""
        # The logic here remains the same.
        # TODO: Create a 'data_to_save' dictionary.
        data_to_save = {
            'students': [],
            'teachers': [],
            'courses': []
        }
        # TODO: Convert self.students, self.teachers, and self.courses into lists of dictionaries.
        for student in self.students:
            student_dict = {
                'id': student.id,
                'name': student.name,
                'instrument': student.instrument
            }
            data_to_save['students'].append(student_dict)
        for teacher in self.teachers:
            teacher_dict = {
                'id': teacher.id,
                'name': teacher.name,
                'specialization': teacher.specialization
            }
            data_to_save['teachers'].append(teacher_dict)
        for course in self.courses:
            course_dict = {
                'id': course.id,
                'name': course.name,
                'instrument': course.instrument,
                'teacher_id': course.teacher_id,
                'weekday': course.weekday,
                'enrolled_student_ids': course.enrolled_student_ids
            }
            if hasattr(course, 'check_ins'):
                course_dict['check_ins'] = course.check_ins
            data_to_save['courses'].append(course_dict)
        # TODO: Write the result to the JSON file.
        try:
            with open(self.data_path, 'w') as f:
                json.dump(data_to_save, f, indent=2)
        except Exception as e:
            print(f"Failed to save data: {e}")

    def register_new_student(self, name, instrument):
        """Registers a new student and returns success status with a message."""
        next_id = f"S{1001 + len(self.students)}"
        has_teacher = any(t.specialization.lower() == instrument.lower() for t in self.teachers)
        if not has_teacher:
            return False, f"No teacher available for {instrument}. Cannot register student."
        new_student = StudentUser(id=next_id, name=name, instrument=instrument)
        self.students.append(new_student)
        self._save_data()
        return True, f"Student {name} (ID: {next_id}) registered successfully."

    def check_in(self, student_id, course_id):
        """Checks in a student for a course and returns success status with a message."""
        student = next((s for s in self.students if s.id == student_id), None)
        course = next((c for c in self.courses if c.id == course_id), None)
        if not student or not course:
            return False, "Student or course not found."
        if student_id not in course.enrolled_student_ids:
            return False, f"Student {student.name} is not enrolled in {course.name}."
        if not hasattr(course, "check_ins"):
            course.check_ins = []
        if student_id in course.check_ins:
            return False, f"Student {student.name} is already checked in for {course.name}."
        course.check_ins.append(student_id)
        self._save_data()
        return True, f"Student {student.name} checked in for {course.name}."

    def add_teacher(self, name, specialization):
        """Adds a new teacher to the system."""
        next_id = f"T{101 + len(self.teachers)}"
        new_teacher = TeacherUser(id=next_id, name=name, specialization=specialization)
        self.teachers.append(new_teacher)
        self._save_data()
        return True, f"Teacher {name} (ID: {next_id}) added successfully."

    def create_course(self, name, instrument, teacher_id, weekday):
        """Creates a new course with the given details."""
        course_id = f"L{self.next_lesson_id}"
        new_course = Course(
            id=course_id,
            name=name,
            instrument=instrument,
            teacher_id=teacher_id,
            weekday=weekday,
            enrolled_student_ids=[]
        )
        self.courses.append(new_course)
        self.next_lesson_id += 1
        self._save_data()
        return True, f"Course {name} (ID: {course_id}) created successfully."

    def enroll_student_in_course(self, student_id, course_id):
        """Enrolls a student in a course."""
        student = next((s for s in self.students if s.id == student_id), None)
        course = next((c for c in self.courses if c.id == course_id), None)
        if not student or not course:
            return False, "Student or course not found."
        if student_id in course.enrolled_student_ids:
            return False, f"Student {student.name} is already enrolled in {course.name}."
        course.enrolled_student_ids.append(student_id)
        self._save_data()
        return True, f"Student {student.name} enrolled in {course.name} successfully."