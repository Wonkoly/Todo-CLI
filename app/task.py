class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def __repr__(self):
        return f"Task(description='{self.description}', completed={self.completed})"
