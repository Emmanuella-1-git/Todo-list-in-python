New! Keyboard shortcuts … Drive keyboard shortcuts have been updated to give you first-letters navigation
# todo_list.py

def display_menu():
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Delete a Task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour To-Do List is empty.\n")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        print()

def add_task(tasks):
    task = input("Enter a task to add: ")
    tasks.append(task)
    print(f'"{task}" has been added to your To-Do List.\n')

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_num = int(input("Enter the number of the task to delete: "))
        if 0 < task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f'"{removed_task}" has been removed from your To-Do List.\n')
        else:
            print("Invalid task number.\n")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            delete_task(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()