# Problem:1--> sum 'n' numbers:
n = int(input("Enter a number : "))
sum = 0
index = 0
while index<=n:
    sum+= index
    index+=1

print(sum)

# with 'for' loop:
sum2 = 0
for i in range(1,n+1):
    sum2 += i

print(sum2)


# Problem:2--> 'n' factorial :
x = int(input("Enter the number : "))

factorial = 1

for i in range(1,n+1):
    factorial *=i

print(factorial)
