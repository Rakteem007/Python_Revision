password = "Raktee"

if len(password) < 6:
    print("Your password is weak")
elif len(password) >= 10 and "$" in password or "#" in password:
    print("Your Password is Strong")
elif len(password) >= 6 and "$" in password or "#" in password:
    print("Your password is medium strong")
elif len(password) >= 6 and "$" not in password or "#" not in password:
    print("Your password is medium")
