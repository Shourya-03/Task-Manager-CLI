import json
from task import Task

class TaskManager:
    def __init__(self, file_path):
        self.tasks = []
        self.file_path = file_path
        self.load_tasks()

    def add_task(self, title, due_date, priority):
        task = Task(title, due_date, priority)
        self.tasks.append(task)

    def show_tasks(self):
        if not self.tasks:
            print("No tasks yet.")
            return
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task.title} | {task.due_date} | {task.priority}")

    def save_tasks(self):
        with open(self.file_path, "w") as f:
            json.dump([t.to_dict() for t in self.tasks], f)

    def load_tasks(self):
        try:
            with open(self.file_path, "r") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(d) for d in data]
        except FileNotFoundError:
            self.tasks = []
