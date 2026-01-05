from manager import ToDoManager

manager = ToDoManager()

while True:
    print("**************************************************")
    print("Welcome to the ToDo App")
    print("To add new task select 1")
    print("To get list of the Tasks select 2")
    print("To mark the task done select 3")
    print("To exit select 4")
    print("***************************************************")
    
    choice = input("make your choice: ")
    
    if choice == "1":
        title = input("Enter task to be added: ")
        manager.add_todo(title)
    elif choice == "2":
        manager.list_all_todos()
    elif choice == "3":
        try:
            index = int(input("Enter the index of the task to be marked done "))
            manager.mark_done(index)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "4":
        print("GoodBuy")
        break
    else:
        print(" Invalid Input")




        
