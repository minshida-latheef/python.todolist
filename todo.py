

tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def delete_task():
    view_tasks()

    if tasks:
        number = int(input("Enter task number to delete: "))
        if 1 <= number <= len(tasks):
            removed = tasks.pop(number - 1)
            print(f"Deleted: {removed}")
        else:
            print("Invalid task number!")

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")