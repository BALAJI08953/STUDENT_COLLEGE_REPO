import json
from student import Student


def save_students(manager):
    student_data = []

    for student in manager.students.values():
        data = {
            "id": student.id,
            "name": student.name,
            "age": student.age,
            "cgpa": student.cgpa,
            "branch": student.branch
        }

        student_data.append(data)

    with open("my_data.json", "w") as file:
        json.dump(student_data, file, indent=4)


def load_students(manager):

    with open("my_data.json", "r") as file:
        student_data = json.load(file)

    for data in student_data:
        student = Student(
            data["id"],
            data["name"],
            data["age"],
            data["cgpa"],
            data["branch"]
        )

        manager.students[student.id] = student