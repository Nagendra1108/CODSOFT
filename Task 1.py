tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added successfully!")


def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task has been removed successfully!")
    else:
        print("Task not found in the list.")


def display_tasks():
    if tasks:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your To-Do List is empty.")

def main():
    while True:
        print("\n=== To-Do List Application ===")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == '3':
            display_tasks()
        elif choice == '4':
            print("Thank you for using the To-Do List Application. Contiue it and aquire new goals. ")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()