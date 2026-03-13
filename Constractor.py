class Myclass:
# without perameter
    def __init__(self):
        print("Constractor is calling")

# with perameter
    def __init__(self, name):
        self.name1 = name



object = Myclass("Arib")
print(object.name1)