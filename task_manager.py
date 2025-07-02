import json
import os
from datetime import datetime

TASK_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False, "created": str(datetime.now())})
    save_tasks(tasks)

def show_tasks():
    tasks = load_tasks()
    for i, task in enumerate(tasks, 1):
        status = "✅" if task["done"] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)

def menu():
    while True:
        print("\n====== TASK TRACKER ======")
        print("1. ➕ Add Task")
        print("2. 📋 Show Tasks")
        print("3. ✅ Mark Task as Done")
        print("4. 🗑️ Delete Task")
        print("5. ❌ Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            index = int(input("Enter task number to mark done: ")) - 1
            mark_done(index)
        elif choice == "4":
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(index)
        elif choice == "5":
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()
