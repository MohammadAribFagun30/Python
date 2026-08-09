class student:

    # Class attribute 
    university_name = "International Islamic Unversity"


    def __init__(self,name,marks):
        self.name = name # object attribute
        self.marks = marks
        



Object1 = student("Fagun","95")
print(Object1.name , Object1.marks)

#To call class attributes-

print(student.university_name)
