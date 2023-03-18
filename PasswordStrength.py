import re

def password_check(password):
    strength = 0
    if len(password) >= 12:
        strength += 1
    if re.search("[a-z]", password):
        strength += 1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[!@#$%^&*()_+]", password):
        strength += 1
    return strength

    
password = input("Enter your password: ")

strength = password_check(password)

print(f"your password has a strength of {strength} out of 5")

if strength < 5:
    print("Consider the following:\n-Password length should be more than 12 characters\n-It needs to have at least one lower-case and upper-case letter\n-It needs to have one number\n-It needs to have one special character")
else:
    print("Nice!! your password is strong.")