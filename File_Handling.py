# syntax-1
# file = open("youtube.txt", "w")

# try:
#     file.write("hey there, i am honu codor")
# finally:
#     file.close()

# syntax-2

with open("youtube.txt", "w") as file:
    file.write("hey there, i am honu codor")

