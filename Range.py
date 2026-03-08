# keywod : range( start,  stop, strp )

# type:1 ->
sequence = range(5)

print( sequence[0]  )
print( sequence[1]  )
print( sequence[2]  )
print( sequence[3]  )
print( sequence[4]  )

# type :2 ->

sequence = range(10) 

for i  in sequence:
    print(i) # 0 1 2 3 4 5 6 7 8 9



# type:3 ->
for i in range(5):   # end :5
    print(i)

# type:4 ->

for i in range(1,10):   # star:1 , end:9
    print(i) # 1 2 3 4 5 6 7 8 9




# type:5 ->

for i in range(1,5,2):   # start: 1 , end: 9 , increment: 2
    print(i) # 1  3 



# printing in reverse :

for i in range(5, 1, -1): 
    print(i) # 5 4 3 2