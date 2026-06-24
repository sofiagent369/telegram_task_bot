import datetime
import json
import os
import logging

# Configurar el logger
logging.basicConfig(filename='log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def format_date(date: datetime.datetime) -> str:
    return date.strftime("%Y-%m-%d %H:%M")

def load_tasks(file_path="tasks.json") -> list:
    if not os.path.exists(file_path):
        logging.warning(f"File {file_path} does not exist, returning empty tasks.")
        return []
    
    with open(file_path, "r") as file:
        try:
            tasks = json.load(file)
            for task in tasks:
                task['reminder'] = datetime.datetime.strptime(task['reminder'], "%Y-%m-%d %H:%M")
            logging.info(f"Loaded {len(tasks)} tasks from {file_path}.")
            return tasks
        except (json.JSONDecodeError, ValueError) as e:
            logging.error(f"Error loading tasks from {file_path}: {e}")
            return []

def save_tasks(tasks: list, file_path="tasks.json") -> None:
    with open(file_path, "w") as file:
        json.dump([task_serializer(task) for task in tasks], file, indent=4)
        logging.info(f"Saved {len(tasks)} tasks to {file_path}.")

def task_serializer(task):
    return {
        'description': task['description'],
        'reminder': task['reminder'].strftime("%Y-%m-%d %H:%M")
    }