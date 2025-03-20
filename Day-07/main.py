print("To-Do List mein Khush amadeed! 📝")
tasks = []
def show_menu():
    print("\nMenu:")
    print("1. Nayi Task Add Karein")
    print("2. Tasks Dekhein")
    print("3. Task Delete karein")
    print("4. Exit")
while True:
    show_menu()
    choice = input ("Apna choice Enter Karein: ")
    if choice == "1":
        new_task = input("Nayi Task Likhein: ")
        tasks.append(new_task)
        print(f"Task Add Hui: '{new_task}'")
    elif choice == "2":
        if tasks:
            print("\nApki Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("\nKoi tasks mojood nahi hain!")

    elif choice == "3":
        if tasks:
            print("\nApki tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            try:
                task_to_delete = int(input("woh task ka number likhein jo delete karna hai: "))  
                if 1 <=  task_to_delete <= len(tasks) :
                    removed_task = tasks.pop(task_to_delete -1)
                    print(f"Task Delete Hui: '{removed_task}'")
                else:
                    print("Invalid Task Number! ")
            except ValueError:
                print("Sirf Value Likhien!")
        else:
            print("\nDelete Karne ke Liye Koi Task Nahi Hain!")
    elif choice == "4":
            print("To-do List App Band ho Raha Hai. Allah Hafiz! 👋")
            break
    else:
            print("Ghalat Choice! Dobara Koshish Karein.")

    
             