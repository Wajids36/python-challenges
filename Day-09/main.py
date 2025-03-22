# Day 09 
# Password Strength Checker

import re 
print("Password Strength Checker  🔐") 
password = input("Apna Password Enter Karein: ") 
if len(password) < 6 or password.isalpha():
    print("Password Strength: Weak ❌")
elif len(password) >= 8 and not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    print("Password Strength: Moderate ⚠")
elif len(password) >= 8 and re.search(r"[A-Z]", password) and re.search(r"[a-z]", password) \
         and re.search(r"[0-9]", password) and re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    print("Password Strength: Strong ✅")
else:
    print("Password Strength: Weak ❌")

