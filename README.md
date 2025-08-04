# FIT1056 Coursework Repository
This repository stores my work for **FIT1056 – Introduction to Software Engineering**.  
I’m keeping everything for the semester in one place, but I’ve separated my personal tasks (PST) from the group project so it’s easier to navigate.


FIT1056_works/
├─ individual/ # All personal task submissions
│ └─ PST1/
│ └─ MSMS.py # Single-file version of the PST1 prototype
└─ project/ # Shared group project space
└─ group_project/





---

## PST1 – Music School Management System (MSMS)

### Project Idea
PST1 is about putting together a small, in-memory prototype of a **Music School Management System**.  
Everything runs locally – no database or files – so once you close the program, the data disappears.  
The focus is on practising how to organise code, keep logic separated, and make a basic interactive menu.

---

### Features Overview
- **Data Models**: simple `Student` and `Teacher` classes  
- **In-memory storage**: lists `student_db` and `teacher_db` with auto-incrementing IDs  
- **Core functions** for:
  - Adding teachers  
  - Listing all students or teachers  
  - Searching (case-insensitive) by name or speciality  
- **Front desk features**:
  - Registering a new student and enrolling them right away  
  - Adding courses to existing students  
  - Combined search for both students and teachers  
- **Menu options** for:
  1. New student registration  
  2. Enrolling an existing student  
  3. Search for people in the system  
  4. Show all students  
  5. Show all teachers  
  q. Quit

---
## How to Run It
**Prerequisite:** Python 3.9 or newer.  
From the repo’s root folder:
```bash
cd FIT1056_works
python individual/PST1/MSMS.py


