class Myclass:

# without perameter-1 :   # Constructor is called "Dunder method"
    def __init__(self):   # This is like [ def Myclass(self) ]
        pass


# without perameter-2 :
    def __init__(self):   # This is like [ def Myclass(self) ]
        print("Constractor is calling")


# with perameter
    def __init__(self, name):
        self.name1 = name



object = Myclass("Arib")
print(object.name1)