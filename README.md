<<<<<<< HEAD
Music School Management System (MSMS)
This project is a GUI-based management system for a music school, built with Python and Streamlit. It simplifies tasks like student registration, course scheduling, and daily lesson check-ins.
🚀 Quick Start
1. Install Dependencies
Ensure you have Python 3.8+ installed. Then install required packages:
bash
pip install streamlit pandas
2. Run the Application
In the project’s root directory, execute:
bash
python -m streamlit run main.py
Streamlit will automatically open a browser window (or use the link http://localhost:8501 from the terminal).
📂 Project Structure
plaintext
msms-project/
├── app/              # Business logic (data models, managers)
│   ├── schedule.py   # Manages courses, student check-ins
│   ├── student.py    # Student data models
│   └── teacher.py    # Teacher & course data models
├── gui/              # Streamlit UI pages
│   ├── main_dashboard.py  # Main navigation dashboard
│   ├── student_pages.py   # Student registration/search UI
│   └── roster_pages.py    # Daily roster/check-in UI
├── data/             # Data persistence (JSON storage)
│   └── msms.json     # Stores students, teachers, courses, and check-in data
└── main.py           # Entry point for the Streamlit app
🌟 Core Features
1. Student Management
Register New Students: Add students with their name and instrument preference.
Search Existing Students: Look up students by name or unique ID.
2. Course & Teacher Management
View Scheduled Courses: See which courses (instrument, teacher, weekday) are available.
Optional Extension: Create/edit courses (if implemented in your version).
3. Daily Roster & Check-In
View Daily Roster: See which students are scheduled for lessons on a specific day.
Mark Student Check-In: Record when a student attends their scheduled lesson.
📝 Data Persistence
All data (students, teachers, courses, check-ins) is stored in data/msms.json. The app reads from and writes to this file to preserve data between sessions.
🛠️ Dependencies
streamlit: Builds the interactive web GUI.
pandas: (Optional) For data manipulation (used if your logic requires it).
python-dateutil/pytz: (Optional) For date/time handling in scheduling.
📌 Notes
Ensure the data/ folder is writable so the app can save changes.
If you get ModuleNotFoundError, use python -m streamlit run main.py to ensure correct module resolution.
For isolated dependencies (recommended), use a virtual environment:
bash
python -m venv venv
source venv/Scripts/activate  # Windows: venv\Scripts\activate
pip install streamlit pandas
=======
# MSMS v2 (Persistent)

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
>>>>>>> 26695019b64377132732ab1397bec5b8ba6afe69
