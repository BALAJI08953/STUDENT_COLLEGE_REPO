# Student Management System

A beginner-to-intermediate Python project for managing student records using Object-Oriented Programming.

The project is being developed incrementally to practice Python concepts by building a real command-line application rather than isolated programs.

## Features

- Add students
- View students
- Search students by ID
- Update student information
- Delete students
- Sort students
- Find the topper
- Calculate average CGPA
- Save student records to JSON
- Load student records from JSON
- Exception handling
- Logging

## Current Progress

Currently implemented:

- Student class
- `__init__()`
- `__str__()`
- `to_dict()`
- StudentManager class
- Add student
- View students
- Search student
- Update student
- Delete student
- Sort students

More features will be added as the project develops.

## Project Structure

```text
student_management/
│
├── main.py
├── student.py
├── manager.py
├── file_handler.py
├── logger_config.py
├── utils.py
│
├── data/
│   └── students.json
│
├── logs/
│   └── student.log
│
├── README.md
└── .gitignore
Concepts Practiced
Python
Variables
Functions
Lists
Dictionaries
Loops
Conditional statements
Lambda functions
sorted()
Exception handling
JSON
File handling
Logging
Object-Oriented Programming
Classes
Objects
Constructors
Instance attributes
Instance methods
self
__init__()
__str__()
to_dict()
Object relationships
Encapsulation
Student Information

Each student contains:

ID
Name
Age
Branch
CGPA

Example:

ID: 23
Name: Bhagirath
Age: 19
Branch: Computer Science
CGPA: 7.41
Application Menu

The planned command-line interface is:

================================
       STUDENT MANAGEMENT
================================

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Sort Students
7. Find Topper
8. Calculate Average CGPA
9. Save Students
10. Load Students
11. Exit
How to Run

Clone the repository:

git clone YOUR_REPOSITORY_URL

Navigate to the project:

cd student_management

Run the program:

python main.py
Purpose

The purpose of this project is to strengthen Python programming and Object-Oriented Programming skills by building a structured application.

Instead of learning concepts only through isolated exercises, this project combines them into one practical system.

Future Improvements
JSON data persistence
Logging system
Input validation
Better exception handling
Student statistics
Search by name or branch
Improved command-line interface
Modular project architecture
Code refactoring
Author

Balaji Bhagirath Bodducherla

Computer Science Engineering Student

