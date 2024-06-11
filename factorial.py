# factorial of a number using while loop 
n = int(input("Enter the number : "))

f=1
while n != 1:
    f *= n
    n -= 1

print("The factorial is ",f)
