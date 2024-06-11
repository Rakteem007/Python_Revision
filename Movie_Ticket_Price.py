age = int(input("Enter the age : "))
day = input("Enter the day : ")

# price = 0

# if age > 18:
#     price=12
# else:
#     price = 8

price = 12 if age >= 18 else 8

if day == "Wednesday":
    price -= 2

print("Your final price is $",price)