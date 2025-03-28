# Day 14
print("Welcome to the Adventure of the lost kingdom! ")
print("You are a brave explorer entering a mysterious forest in search of treasure.")
print("Choose wisely, your decisions will shape your fate!")
choice1 = input("You encounter two paths. Do you go left (type 'left') or do you go right (type 'right')?").lower()
if choice1 == "left":
    print("You walk into a dark cave and find a hidden chest. But there's a sleeping dragon!")
    choice2 = input("Do you sneak to the treasure (type 'sneak') or try to fight the dragon (type 'fight')? ").lower()
    if choice2 == "sneak":
     print("You sucessfully sneak the past and take the treasure. You won!")
    elif choice2 == "fight":
     print("The dragon wakes up and defeated you. Game over!")
    else:
     print("Invalid choice. The advanture ends. ")
elif choice1 == "right":
   print("You follow a sunny path and encounter a wise old sage. ")
   choice2 = input("Do you ask for help (type 'ask') or ignore the sage and keep walking (type 'ignore')?").lower()
   if choice2 == "ask":
      print("The sage gives you a map to the treasure.You find it and win!")
   elif choice2 ==  "ignore":
      print("Without guidance, you lost in the forest. Game over!") 
   else:
      print("Invalid choice. The advanture ends!")   
else:
   print("Invalid choice. The advanture ends!")

