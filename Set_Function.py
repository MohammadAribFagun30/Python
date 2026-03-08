null_set = set()

# add element in set :

null_set.add(1)
null_set.add(2)
null_set.add(3)

print(null_set) # {1, 2, 3}


# remove element from set :

#               value
null_set.remove(  3   )

print(null_set) # {1, 2}


# clearing a set
set1 = {1,2,3,4,5}
set1.clear()

print(set1) # will print---> set()

# remove a random element :
set2 = {1,2,3,4,5}
set2.pop()

print(set2)


# *important*  union methods :
set1 = {1,2,3}
set2 = {3,4,5}

print( set1.union( set2 ) ) # {1, 2, 3, 4, 5}

# intersection method :
set1 = {1,2,3}
set2 = {3,4,5}

print( set1.intersection(set2) ) # { 3 }



