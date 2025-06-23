import os
from manager import TaskManager

# Task Manager CLI Application
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
TASKS_FILE = os.path.join(BASE_DIR, "tasks.json")

manager = TaskManager(TASKS_FILE)

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Save Tasks")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":
        title = input("Task title: ")
        date = input("Due date: ")
        priority = input("Priority (High/Med/Low): ")
        manager.add_task(title, date, priority)

    elif choice == "2":
        manager.show_tasks()

    elif choice == "3":
        manager.save_tasks()
        print("Tasks saved to file.")

    elif choice == "4":
        break

    else:
        print("Invalid choice.")
