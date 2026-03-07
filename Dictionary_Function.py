profile = {

    "Name" : "Mohammad Arib Fagun",
    "CGPA" : 4,
    "Semester" : "2nd",
    "Subject" : ["DLD","Chemistry", "Statistics","GEED"], #tuples
    "Topper" : ("Labib", "Fahmid","Towhid","Albab") # list
}

print( profile.keys() ) # returns keys
print( len( profile.keys() ) ) # return keys length

print( profile.values()  ) # return values

print( profile.items() ) # returns "keys" and "values"

print()

# Update in Dictionary :

# Method :1 -->
person = {'name': 'Alice', 'age': 25}
update_data = {'age': 26, 'city': 'New York'}

person.update(update_data)
print(person) # {'name': 'Alice', 'age': 26, 'city': 'New York'}
 
print()
# Method :2 -->
person = {'name': 'Alice', 'age': 25}
person.update( [ ('age', 30) , ('country', 'USA') ] ) 
print(person) # {'name': 'Alice', 'age': 30, 'country': 'USA'}

print()
# Method :3 -->
person = {'name': 'Alice', 'age': 25}
person.update( age=28 ,  city='London' )
print(person) # {'name': 'Alice', 'age': 28, 'city': 'London'}
