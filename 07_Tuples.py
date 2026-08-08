# Tuple is immutable


tuple = (1,2,3,4,5)
print(tuple)

# Can not do like list
# tuple[0] = 5


print(tuple[0])
print(tuple[1])


# Tuple Slicing
print( tuple[1:5] )


                # value
print( tuple.index(3) )  # print index


tuple2 = (1,2,3,4,5,5)
print( tuple2.count(5) )


# User input

li = ()

for i in range(5):
    y = input("Enter value: ")

    # Convert value to int or float if possible
    try:
        y = int(y)
    except ValueError:
        try:
            y = float(y)
        except ValueError:
            pass
    li = li + (y,)

    

print(li)