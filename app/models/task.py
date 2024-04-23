class Task:
    def __init__(self,owner, name, status, desc, priority, due_date):
        self.owner = owner
        self.name = name
        self.status = status
        self.desc = desc
        self.priority = priority
        self.due_date = due_date