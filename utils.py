import datetime
import json
import os

def format_date(date: datetime.datetime) -> str:
    return date.strftime("%Y-%m-%d %H:%M")

def load_tasks(file_path="tasks.json") -> list:
    if not os.path.exists(file_path):
        return []
    
    with open(file_path, "r") as file:
        try:
            tasks = json.load(file)
            for task in tasks:
                task['reminder'] = datetime.datetime.strptime(task['reminder'], "%Y-%m-%d %H:%M")
            return tasks
        except (json.JSONDecodeError, ValueError):
            return []

def save_tasks(tasks: list, file_path="tasks.json") -> None:
    with open(file_path, "w") as file:
        json.dump([task_serializer(task) for task in tasks], file, indent=4)

def task_serializer(task):
    return {
        'description': task['description'],
        'reminder': task['reminder'].strftime("%Y-%m-%d %H:%M")
    }