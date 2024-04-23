from app.models.task import Task

import json
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, owner, name, status, desc, priority, due_date):
        task = Task(owner, name, status, desc, priority, due_date)
        self.tasks.append(task)

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            return f"Task Deleted.\n"
        else:
            return f"Invalid Index: {index}\n"

    def edit_task(self, index, field, value):
        if 0 <= index < len(self.tasks):
            setattr(self.tasks[index], field, value)
            return f"Task {field.upper()} successfully changed.\n"
        else: 
            return f"Invalid Index: {index}\n"
        
    def change_status (self, index, status):
        return self.edit_task(index, "status", status)

    def show_tasks(self):
        task_list = []
        for i, task in enumerate(self.tasks):
            task_list.append({
                "owner": task.owner,
                "name": task.name,
                "status": task.status,
                "desc": task.desc,
                "priority": task.priority,
                "due_date": task.due_date
            })
        return task_list


    def save(self):
        json_tasks = []

        for task in self.tasks:
            json_task = {
                "owner": task.owner,
                "name": task.name,
                "status": task.status,
                "desc": task.desc,
                "priority": task.priority,
                "due date": task.due_date
            }
            json_tasks.append(json_task)

        with open("tasks.json", "w") as file:
            json.dump(json_tasks, file)
    
    def load(self):
        try:
            with open("tasks.json", 'r') as file:
                json_tasks = json.load(file)
                for json_task in json_tasks:
                    self.add_task(json_task['owner'], json_task['name'], json_task['status'], json_task['desc'],
                                  json_task['priority'], json_task['due_date'])
        except FileNotFoundError:
            return "Error, file not found."
    
    def due_date_notification(self):
        notification_list = []
        for task in self.tasks:
            date_now = datetime.now.date()
            due_date = datetime.strptime(task.due_date, "%Y-%m-%d").date()
            difference = (due_date - date_now).days
            if difference <= 1:
                notification_list.append(f"This task: *{task.name}* is approaching is due date -> {task.due_date}")
        return notification_list