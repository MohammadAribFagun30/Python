list = [1,3,2,4]

list.append(5)  # add 5 in last of the list-> [1,2,3,4,5]
print(list)

list.sort() 
print(list)


list.reverse()  # sort in decending order
print(list)

#          index  value
list.insert(  2  ,   10)   # will insert 10 in index 2
print(list)



list2 = [1,2,2,3,4]

c = list2.count(2)
print(c)

list2.remove(2) # will remove the 1st 2 in the list-> [1,2,3,4]
print(list2)

#       index
list2.pop( 3 ) # remove the value of index 3
               # If we donot give any index, it will pop last element
print(list2)



list3 = [1,2,3,4]
print(sum(list3)) # will print sum (10)



