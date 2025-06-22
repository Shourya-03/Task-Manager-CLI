class Task:
    def __init__(self, title, due_date, priority):
        self.title = title
        self.due_date = due_date
        self.priority = priority

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, due_date, priority):
        task = Task(title, due_date, priority)
        self.tasks.append(task)

    def show_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task.title} | {task.due_date} | {task.priority}")

# Main program
manager = TaskManager()

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Choose (1/2/3): ")

    if choice == "1":
        title = input("Task title: ")
        date = input("Due date: ")
        priority = input("Priority (High/Med/Low): ")
        manager.add_task(title, date, priority)
    elif choice == "2":
        manager.show_tasks()
    elif choice == "3":
        break
    else:
        print("Invalid choice.")
