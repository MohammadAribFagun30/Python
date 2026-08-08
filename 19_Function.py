# Define function

# function without perameter:

def print_one():
    print("Function Calling !!")


print_one() # Function Calling !!



# function with perameter :

def suming ( a,b):
    sum = a+b
    return sum


calculate_sum = suming(3,5)
print(calculate_sum)



def find_factorial(a):
    factorial  = 1
    for i in range(1,a+1):
        factorial*=i
    print(factorial)

    return factorial
    

n = int(input("Enter a number : "))
result = find_factorial(n)


# EVEN or ODD

def check(a):
    if(a%2==0):
        print("EVEN")
    else:
        print("ODD")

n = int(input("Enter the number : "))

check(n)