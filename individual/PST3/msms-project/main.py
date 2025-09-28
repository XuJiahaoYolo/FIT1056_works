from app.schedule import ScheduleManager

def front_desk_daily_roster(manager, day):
    courses = manager.get_lessons_by_day(day)
    print(f"\n--- Daily Roster for {day} ---")
    if not courses:
        print("(no lessons)")
        return
    print("-" * 80)
    print(f"{'Time':<8} | {'Course':<20} | {'Room':<8} | {'Teacher':<15} | Students")
    print("-" * 80)
    for c in sorted(courses, key=lambda x: x.time):
        teacher_name = next((t.name for t in manager.teachers if t.user_id == c.teacher_id), c.teacher_id)
        student_names = []
        for sid in c.student_ids:
            st = manager.find_student_by_id(sid)
            student_names.append(st.name if st else sid)
        print(f"{c.time:<8} | {c.name:<20} | {c.room:<8} | {teacher_name:<15} | {', '.join(student_names)}")
    print("-" * 80)

def switch_course(manager, student_id, from_course_id, to_course_id):
    s = manager.find_student_by_id(student_id)
    c_from = manager.find_course_by_id(from_course_id)
    c_to = manager.find_course_by_id(to_course_id)
    if not s or not c_from or not c_to:
        print("Error: invalid student/course id.")
        return
    if from_course_id in s.enrolled_course_ids:
        s.drop(from_course_id)
        if student_id in c_from.student_ids:
            c_from.student_ids.remove(student_id)
    if to_course_id not in s.enrolled_course_ids:
        s.enroll(to_course_id)
        if student_id not in c_to.student_ids:
            c_to.student_ids.append(student_id)
    manager._save_data()
    print(f"Success: switched {s.name} from {c_from.name} -> {c_to.name}.")

def check_in_prompt(manager):
    student_id = input("Enter student ID: ").strip()
    course_id = input("Enter course ID: ").strip()
    manager.check_in(student_id, course_id)

def list_all_basic(manager):
    print("\n-- Students --")
    for s in manager.students:
        print(f"{s.user_id}: {s.name}  <{s.email}>  enrolled={s.enrolled_course_ids}")
    print("\n-- Teachers --")
    for t in manager.teachers:
        print(f"{t.user_id}: {t.name}  instruments={getattr(t, 'instruments', [])}  course_ids={getattr(t, 'course_ids', [])}")
    print("\n-- Courses --")
    for c in manager.courses:
        print(f"{c.course_id}: {c.name}  {c.day} {c.time}  room={c.room}  teacher={c.teacher_id}  students={c.student_ids}")

def main():
    manager = ScheduleManager()
    while True:
        print("\n===== MSMS v3 (Object-Oriented) =====")
        print("1) Show daily roster")
        print("2) Check-in a student")
        print("3) Switch a student's course")
        print("4) Quick view: all data")
        print("Q) Quit")
        choice = input("Enter choice: ").strip().lower()
        if choice == '1':
            day = input("Enter day (e.g., Monday): ").strip()
            front_desk_daily_roster(manager, day)
        elif choice == '2':
            check_in_prompt(manager)
        elif choice == '3':
            sid = input("Student ID: ").strip()
            from_cid = input("From Course ID: ").strip()
            to_cid = input("To Course ID: ").strip()
            switch_course(manager, sid, from_cid, to_cid)
        elif choice == '4':
            list_all_basic(manager)
        elif choice == 'q':
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
