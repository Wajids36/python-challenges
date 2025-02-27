# Day 3 – Daily Python Challenge 
#Challenge: Aisa Python program likho jo user se ek number le aur check kare ke wo prime
#  number hai ya nahi





def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i ==0:
            return False
        return True

user_number = int(input("Enter a Number:"))
if is_prime(user_number):
    print("Yes, It's a Prime Number")
else:
    print("No, It's Not a Prime Number")


    
