str = "Mohammad"
print(str[0 : 5]) #ekne 0 index theke (5-1) index prjanto print hbe

print(str[:5]) # same as [0:5]

#Negative index
# M  o  h  a  m  m  a d
#-8 -7 -6 -5 -4 -3 -2 -1

print(str[-3 : -1]) # will print --> "ma"


# SKip Value

print(str[0 : 8 : 2 ]) # ekne [0:8] diye index(0)--index(7) prjanto include
                       # 2 diye 2ta kore value skip kore print hbe
                       # will print --> "Mhma"