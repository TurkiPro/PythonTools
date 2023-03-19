import re
import hashlib
import requests

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

def pwned_api_check(password):
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    head = sha1_password[:5]
    tail = sha1_password[5:]
    url = 'https://api.pwnedpasswords.com/range/'  + head
    resource = requests.get(url)
    hashes = (line.split(':') for line in resource.text.splitlines())
    
    for i, count in hashes:
        if i == tail:
            return count
    return 0

    
password = input("Enter your password: ")

strength = password_check(password)
compromised = pwned_api_check(password)

print(f"your password has a strength of {strength} out of 5")

if compromised:
    print(f"\n{compromised} breaches found for this password. You should change it.\n")
else:
    print("\nNo breaches found for this password.\n")

if strength < 5:
    print("\nConsider the following:\n-Password length should be more than 12 characters\n-It needs to have at least one lower-case and upper-case letter\n-It needs to have one number\n-It needs to have one special character\n")
else:
    print("\nNice!! your password is strong.\n")