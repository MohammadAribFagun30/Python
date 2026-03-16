class python:
    # Custom method without paranter-
    def welcome(self):
        print("Welcome to Learn python !")



    # Custom method without paranter-
    def welcome(self):
        print("Welcome to Learn python !", self.name)



    # Custom methods with parameter-
    def display(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa



# creating object-
object = python()


# Calling the methods with parameter-
object.display("Fagun",4)
print(object.name, object.cgpa)

# do not do this
print(object.display("Fagun",4))   # print-> None


# calling the methods without parameter-
object.welcome()