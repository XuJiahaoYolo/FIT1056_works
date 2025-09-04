# MSMS — PST3 (Object-Oriented Refactor)

An object-oriented refactor of the Music School Management System (MSMS).
PST2’s procedural code is reorganized into a three-layer architecture: **Model / Controller / View**, with data persisted to `data/msms.json`.

## Project Structure
```
msms-project/
├─ app/                   # Python package (Model + Controller)
│  ├─ __init__.py
│  ├─ user.py             # Base User
│  ├─ student.py          # StudentUser (inherits User)
│  ├─ teacher.py          # TeacherUser and Course
│  └─ schedule.py         # ScheduleManager: load/save/check-in/query
├─ data/
│  └─ msms.json           # Data: students/teachers/courses/attendance
└─ main.py                # View: front-desk menu and I/O
```

## Requirements
- Python **3.10+** (3.11/3.12 recommended)
- No third‑party dependencies (standard library only)

## Quick Start
From the project root `msms-project/`:

```bash
# Windows
python main.py
# or
py main.py
```

> **VS Code tip:** run in the **Terminal** (not the Output panel).
> Right‑click `main.py` → “Run Python File in Terminal”, or open **Terminal** and run `python main.py`.

You’ll see:
```
1) Show daily roster
2) Check-in a student
3) Switch a student's course
4) Quick view: all data
Q) Quit
```

## Sample Data (`data/msms.json`)
Use this minimal dataset to run immediately:

```json
{
  "students": [
    {
      "type": "StudentUser",
      "user_id": "S001",
      "name": "Alice",
      "email": "alice@example.com",
      "enrolled_course_ids": ["C-Piano-1"],
      "grade_level": "Beginner"
    }
  ],
  "teachers": [
    {
      "type": "TeacherUser",
      "user_id": "T001",
      "name": "Mr. Brown",
      "email": "brown@example.com",
      "instruments": ["Piano"],
      "course_ids": ["C-Piano-1"]
    }
  ],
  "courses": [
    {
      "course_id": "C-Piano-1",
      "name": "Piano Basics",
      "day": "Monday",
      "time": "15:30",
      "room": "R101",
      "teacher_id": "T001",
      "student_ids": ["S001"]
    }
  ],
  "attendance": []
}
```

## Features
- **Show daily roster** — Pretty table by weekday (course/time/room/teacher/students).
- **Check-in a student** — Validate IDs, append an ISO8601 timestamp record to `attendance`, persist immediately.
- **Switch a student’s course** — Move a student from course A to B; updates both the student and course membership lists; persists.
- **Quick view** — Print summaries of students, teachers, and courses.

## Design Notes
- `StudentUser`, `TeacherUser`, and `Course` implement `to_dict()` / `from_dict()` for JSON ↔ objects.
- `ScheduleManager`:
  - `_load_data()` reads from `data/msms.json` with safe `.get()`.
  - `_save_data()` serializes models back to JSON.
  - Helpers: `find_student_by_id`, `find_course_by_id`, `get_lessons_by_day`.
  - `check_in(student_id, course_id)` validates & records attendance.
- `main.py` is the **View**: collects user input and delegates to the manager.

## Troubleshooting
- **`ModuleNotFoundError: No module named 'app'`**
  - Run from the project root and ensure `app/__init__.py` exists.
- **`JSONDecodeError`**
  - Your JSON has a syntax error (missing comma or quote). Replace with the sample above.
- **VS Code doesn’t accept input**
  - You ran in the *Output* panel. Run in the **Terminal** instead.

## Suggested `.gitignore`
```
__pycache__/
*.pyc
.venv/
.DS_Store
```

## Checkpoints (suggested commit messages)
- `PST3-3.1`: Add Model classes and `msms.json`
- `PST3-3.2`: Implement `_load_data/_save_data` + `attendance_log`
- `PST3-3.3`: Implement `check_in` + validation + persistence
- `PST3-3.4`: Implement `main.py` view (menu, roster, check-in, switch)

## License
For coursework use only.
