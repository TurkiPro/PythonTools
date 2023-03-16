import re

def password_check(password):
    if len(password) < 12:
        return False
    elif not re.search("[a-z]", password):
        return False
    elif not re.search("[A-Z]", password):
        return False
    elif not re.search("[0-9]", password):
        return False
    elif not re.search("[!@#$%^&*()-_=+:;,./?]", password):
        return False
    else:
        return True
    
password = input("Enter your password: ")

if password_check(password):
    print("Your password is strong")
else:
    print("Your password is weak")