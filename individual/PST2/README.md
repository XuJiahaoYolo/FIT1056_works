# MSMS v2 (Persistent)
https://github.com/XuJiahaoYolo/FIT1056_works
## Description
This is a simple Python-based Music School Management System (MSMS) that stores data persistently.  
It allows you to manage students, teachers, and attendance records with basic operations.

## Features
- **Check-in Student**: Record a student's attendance for a course.
- **Print Student Card**: Generate a text file with student details.
- **Update Teacher Info**: Modify teacher name or speciality.
- **Remove Student**: Delete a student from the system.
- **Persistent Storage**: Data is saved and loaded automatically.

## How to Run
1. Make sure you have **Python 3** installed.
2. Place all source files in the same folder.
3. Open a terminal in the project folder.
4. Run:
   ```bash
   python pst2_main.py
   ```

## File Structure
- `pst2_main.py` – Main program file with menu and functions.
- `data.json` – Stores all persistent data (students, teachers, attendance).
- `README.md` – Project instructions.

## Notes
- All data changes are saved automatically after each operation.
- If a record is not found, the program will display an error message.
