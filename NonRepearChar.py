# find the first non-repeated character

input = input("Enter the string : ")

for char in input:
    if input.count(char) == 1:
        print("the first non-repeated character is : ",char)
        exit()