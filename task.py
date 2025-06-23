class Task:
    def __init__(self, title, due_date, priority):
        self.title = title
        self.due_date = due_date
        self.priority = priority

    def to_dict(self):
        return {
            "title": self.title,
            "due_date": self.due_date,
            "priority": self.priority
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["due_date"], data["priority"])
