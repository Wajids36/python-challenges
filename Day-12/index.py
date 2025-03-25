# Password strength checker
# challenge day-12
def password_strength_checker(password):
    has_digit = any(cahr.isdigit() for cahr in password)
    has_uppercase = any(char.isupper() for char in password)
    has_special_char = any(char in"!@#$%^&*()" for char in password)
    if len(password) < 6 :
        return "strength: Weak"
    elif 6 <= len(password) <= 10 and has_digit:
        return "Strength: Medium"
    elif len(password) > 10 and has_digit and has_uppercase and has_special_char:
        return "Strength: Strong"
    else:
        return "Strength: Weak"
password = input("Enter Your Password: ")
print(password_strength_checker(password))