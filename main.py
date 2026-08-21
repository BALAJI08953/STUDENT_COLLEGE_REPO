from student import Student
from manager import student_manager
from flie_handler import save_students, load_students
from logger_config import setup_logger

manager = student_manager()
logger = setup_logger()

def display_menu():
    print("\n================================")
    print("       STUDENT MANAGEMENT")
    print("================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Sort Students")
    print("7. Find Topper")
    print("8. Calculate Average CGPA")
    print("9. Save Students")
    print("10. Load Students")
    print("11. Exit")


while True:
    display_menu()
    choice = input("ENTER YOUR CHOICE: ")
    if choice == "1":
        student_id = int(input("ENTER STUDENT ID: "))
        name = input("ENTER STUDENT NAME: ")
        age = int(input("ENTER AGE: "))
        cgpa = float(input("ENTER CGPA: "))
        branch = input("ENTER BRANCH: ")
        student = Student(student_id, name, age, cgpa, branch)
        manager.add_student(student)
        logger.info(f"Student {student_id} added")

    elif choice == "2":
        manager.display_students()
    elif choice == "3":
        student_id = int(input("ENTER STUDENT ID: "))
        manager.search_student(student_id)
    elif choice == "4":
        student_id = int(input("ENTER STUDENT ID: "))
        newname = input("ENTER NEW NAME: ")
        newage = int(input("ENTER NEW AGE: "))
        newbranch = input("ENTER NEW BRANCH: ")
        newcgpa = float(input("ENTER NEW CGPA: "))
        manager.update_student(
            student_id,
            newname,
            newage,
            newbranch,
            newcgpa
        )
        logger.info(f"Student {student_id} updated")
    elif choice == "5":
        student_id = int(input("ENTER STUDENT ID: "))
        manager.delete_student(student_id)
        logger.info(f"Delete operation performed for student {student_id}")
    elif choice == "6":
        manager.sort_students()
    elif choice == "7":
        manager.topper_student()
    elif choice == "8":
        manager.average_cgpa()
    elif choice == "9":
        save_students(manager)
        logger.info("Students saved")
    elif choice == "10":
        load_students(manager)
        logger.info("Students loaded")
    elif choice == "11":
        print("EXITING STUDENT MANAGEMENT SYSTEM")
        logger.info("Application exited")
        break
    else:
        print("INVALID CHOICE")
        logger.warning("Invalid menu choice entered")