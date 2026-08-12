class Employee:
    def get_designatio(self):
        print("Designatio = Employee")


class Teacher(Employee):
    def get_designatio(self):
        print("Designation = Teacher")



t1 = Teacher()
t1.get_designatio() # Designation = Teacher

t2 = Employee()
t1.get_designatio() # Designation = Teacher