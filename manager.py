from student import *
from flie_handler import save_students,load_students
class student_manager():
    def __init__(self):
        self.students={}
    def add_student(self, student):
        if student.id in self.students:
            print("STUDENT ALREADY PRESENT")
        else:
            self.students[student.id] = student
            print(f"STUDENT ID :{student.id}, STUDENT NAME:{student.name}")
            print("STUDENT SUCCESSFULLY ADDED")
    def search_student(self,student_id):
        if student_id in self.students:
            print("student found")
            student=self.students[student_id]
            print(f"student details:{student.id},{student.name},{student.branch}")
        else:
            print("STUDENT NOT FOUND")
    def update_student(self,student_id,newname,newage,newbranch,newcgpa):
        if student_id in self.students:
            student=self.students[student_id]
            student.name=newname
            student.age=newage
            student.branch=newbranch
            student.cgpa=newcgpa
            print(f"updated the student id {student.id}")
        else:
            print("STUDENT NOT FOUND")
    def delete_student(self,student_id):
        if student_id in self.students:
            student=self.students[student_id]
            print(f"student deleted from the database {student.id}")
            del(self.students[student_id])
            
        else:
            print("student not found")
    def sort_students(self):
        sorted_students = sorted(
            self.students.values(),
            key=lambda student: student.cgpa,
            reverse=True
    )

        for student in sorted_students:
            print(f"{student.id}, {student.name}, {student.cgpa}")


    def display_students(self):

        if not self.students:
            print("NO STUDENTS FOUND IN THE DATA SORRY")
        else:
            for name in self.students.values():
                print(name)
        
    def topper_student(self):
        topper_student=max(self.students.values(),key=lambda student:student.cgpa)
      
        print(f"TOPPER OF THE UNIVERSITY IS: {topper_student.name} ")

    
    def average_cgpa(self):
        total = 0

        for student in self.students.values():
            total += student.cgpa

        print(f"THE AVERAGE OF THE CLASS IS: {total / len(self.students)}")
    


        

        


student1=Student(23,"balaji",19,7.41,"computer science")
student2=Student(24,"gagan",2,7,"civil")
student3=Student(25,"abhi ram",3,5,"aiml")
student10=Student(26,"john",19,7.85,"electronics and communication")
student4=Student(45,"jack",25,8.5,"mechanical")
student5=Student(123,"peter",19,7.93,"elctrical and eletronics")
student6=Student(78945,"mark",24,7.93,"csd")
student7=Student(489,"sam-altomen",26,9.5,"machine learning and atrifical inteligence")
student8=Student(415,"melon musk",19,7.42,"aero-space")
student9=Student(789,"homi bhaba",25,9.58,"chemical")

test=student_manager()
test.add_student(student1)
test.add_student(student2)
test.add_student(student3)
test.add_student(student10)
test.add_student(student4)
test.add_student(student5)
test.add_student(student6)
test.add_student(student7)
test.add_student(student8)
test.add_student(student9)
test.search_student(23)

print()
test.sort_students()
print()
test.display_students()
test.topper_student()
print()
test.average_cgpa()
save_students(test)
manager2 = student_manager()

load_students(manager2)
print("working")

manager2.display_students()

print()

print("worked")