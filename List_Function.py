list = [1,3,2,4]

list.append(5)  # add 5 in last of the list-> [1,2,3,4,5]
print(list)

list.sort() 
print(list)

list.sort(reverse = True) # sort in decending order
list.reverse()  # sort in decending order
print(list)

list.insert(2,10)
print(list)


list2 = [1,2,2,3,4]
list2.remove(2) # will remove the 1st 2 in the list-> [1,2,3,4]
print(list2)
#       index
list.pop( 3 ) # remove the value of index 3
print(list)


