# app/schedule.py
import json
import datetime
from typing import List, Optional

from app.student import StudentUser
from app.teacher import TeacherUser, Course


class ScheduleManager:
    """The main controller for all business logic and data handling."""
    def __init__(self, data_path="data/msms.json"):
        self.data_path = data_path
        self.students: List[StudentUser] = []
        self.teachers: List[TeacherUser] = []
        self.courses: List[Course] = []

        # Initialize the new attendance_log attribute as an empty list.
        # Each record: {"student_id": str, "course_id": str, "timestamp": iso8601 str}
        self.attendance_log: List[dict] = []

        # Load everything from JSON
        self._load_data()

    # ----------------------------
    # Persistence
    # ----------------------------
    def _load_data(self) -> None:
        """Loads data from the JSON file and populates the object lists."""
        try:
            with open(self.data_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Load students, teachers, and courses as objects
            self.students = [
                StudentUser.from_dict(s) for s in data.get("students", []) or []
            ]
            self.teachers = [
                TeacherUser.from_dict(t) for t in data.get("teachers", []) or []
            ]
            self.courses = [
                Course.from_dict(c) for c in data.get("courses", []) or []
            ]

            # Correctly load the attendance log (backward compatible if key missing)
            self.attendance_log = data.get("attendance", []) or []

        except FileNotFoundError:
            print("Data file not found. Starting with a clean state.")

    def _save_data(self) -> None:
        """Converts object lists back to dictionaries and saves to JSON."""
        data_to_save = {
            "students": [
                s.to_dict() if hasattr(s, "to_dict") else s.__dict__ for s in self.students
            ],
            "teachers": [
                t.to_dict() if hasattr(t, "to_dict") else t.__dict__ for t in self.teachers
            ],
            "courses": [
                c.to_dict() if hasattr(c, "to_dict") else c.__dict__ for c in self.courses
            ],
            # Add the attendance_log to the dictionary to be saved.
            # It's already a list[dict], so no further conversion needed.
            "attendance": self.attendance_log,
        }

        with open(self.data_path, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, indent=4, ensure_ascii=False)

    # ----------------------------
    # Helpers / Queries
    # ----------------------------
    def find_student_by_id(self, student_id: str) -> Optional[StudentUser]:
        for s in self.students:
            if s.user_id == student_id:
                return s
        return None

    def find_course_by_id(self, course_id: str) -> Optional[Course]:
        for c in self.courses:
            if c.course_id == course_id:
                return c
        return None

    def get_lessons_by_day(self, day: str) -> List[Course]:
        """Convenience for the View layer: return all courses running on a given day."""
        day_norm = (day or "").strip().lower()
        return [c for c in self.courses if c.day.strip().lower() == day_norm]

    # ----------------------------
    # Core business logic
    # ----------------------------
    def check_in(self, student_id: str, course_id: str) -> bool:
        """
        Records a student's attendance for a course after validation.
        """
        student = self.find_student_by_id(student_id)
        course = self.find_course_by_id(course_id)

        if not student or not course:
            print("Error: Check-in failed. Invalid Student or Course ID.")
            return False

        timestamp = datetime.datetime.now().isoformat(timespec="seconds")
        record = {
            "student_id": student_id,
            "course_id": course_id,
            "timestamp": timestamp,
        }

        self.attendance_log.append(record)
        self._save_data()
        print(f"Success: Student {student.name} checked into {course.name}.")
        return True
