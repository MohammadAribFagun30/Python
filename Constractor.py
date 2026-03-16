class Myclass:
# without perameter-1 :
    def __init__(self):   # This is like [ def student(self) ]
        pass


# without perameter-2 :
    def __init__(self):   # This is like [ def student(self) ]
        print("Constractor is calling")


# with perameter
    def __init__(self, name):
        self.name1 = name



object = Myclass("Arib")
print(object.name1)