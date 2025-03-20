
import random 
# welcome message 
print("Number Guessing Game mein Khush amadeed! 🎯")
# Random number generate krna 
secret_number = random.randint(1, 100)
#Game loop
while True:
    try:
        guess = int(input("Ek Number Guess Karein (1 se 100 ke darmiyan):"))
        if guess < secret_number:
            print("Too Low! Try Again.")
        elif guess > secret_number:
            print("Too High! Try Again.")
        else:
            print("Congratulations! You Guessed it Right! 🎉")
            break
    except ValueError:
        print("Sirf numbers enter karein!")