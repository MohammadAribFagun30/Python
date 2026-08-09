# problrm 1:
# sum n numbers-->

def sum_num( a):
    sum = 0
    if(a==0):
     return 0
    
    return a + sum_num(a-1)

   
number = int(input("Enter a number : "))
result = sum_num(number)
print(result)


# problem 2:
# print all elements of a list -->

def print_list(list,index = 0):
   if(index == len(list)):
      return
   print(list)
   return print_list(list,index+1)


name= ["Arib","Fagun","Alif","Tayeef"]
print(name)


