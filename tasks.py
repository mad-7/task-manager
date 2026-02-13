#!/usr/bin/env python3
import json
import os
from datetime import datetime


TASKS_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)
            return tasks
    except json.JSONDecodeError:
        print(f"Warning: {TASKS_FILE} is corrupted. Starting with empty task list.")
        return []
    except Exception as e:
        print(f"Error loading tasks: {e}")
        return []


def save_tasks(tasks):
    try:
        with open(TASKS_FILE, 'w') as file:
            json.dump(tasks, file, indent=2)
        return True
    except Exception as e:
        print(f"Error saving tasks: {e}")
        return False


def add_task():
    print("\n--- Add New Task ---")
    task_name = input("Enter task description: ").strip()
    
    if not task_name:
        print("Error: Task description cannot be empty!")
        return
    
    tasks = load_tasks()
    
    new_task = {
        "id": len(tasks) + 1,
        "description": task_name,
        "status": "pending",
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    tasks.append(new_task)
    
    if save_tasks(tasks):
        print(f"✓ Task added successfully! (ID: {new_task['id']})")
    else:
        print("✗ Failed to save task.")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("\nNo tasks found. Add your first task!")
        return

    print("\n--- Task List ---")
    print(f"{'ID':<5} {'Status':<10} {'Description':<40} {'Created':<20}")
    print("-" * 75)
    
    for task in tasks:
        status_symbol = "✓" if task['status'] == 'done' else "○"
        status_text = f"{status_symbol} {task['status']}"
        print(f"{task['id']:<5} {status_text:<10} {task['description']:<40} {task['created_at']:<20}")
    
    print(f"\nTotal tasks: {len(tasks)} | Completed: {sum(1 for t in tasks if t['status'] == 'done')}")


def mark_task_done():

    tasks = load_tasks()
    
    if not tasks:
        print("\nNo tasks available to mark as done.")
        return
    
    list_tasks()
    
    try:
        task_id = int(input("\nEnter task ID to mark as done: "))
        
        task_found = False
        for task in tasks:
            if task['id'] == task_id:
                task_found = True
                if task['status'] == 'done':
                    print(f"Task #{task_id} is already marked as done!")
                else:
                    task['status'] = 'done'
                    if save_tasks(tasks):
                        print(f"✓ Task #{task_id} marked as done!")
                    else:
                        print("✗ Failed to update task.")
                break
        
        if not task_found:
            print(f"Error: Task with ID {task_id} not found!")
            
    except ValueError:
        print("Error: Please enter a valid task ID (number)!")
    except Exception as e:
        print(f"Error: {e}")


def delete_task():
    tasks = load_tasks()
    
    if not tasks:
        print("\nNo tasks available to delete.")
        return
    
    list_tasks()
    
    try:
        task_id = int(input("\nEnter task ID to delete: "))
        
        initial_length = len(tasks)
        tasks = [task for task in tasks if task['id'] != task_id]
        
        if len(tasks) < initial_length:
            if save_tasks(tasks):
                print(f"✓ Task #{task_id} deleted successfully!")
            else:
                print("✗ Failed to delete task.")
        else:
            print(f"Error: Task with ID {task_id} not found!")
            
    except ValueError:
        print("Error: Please enter a valid task ID (number)!")
    except Exception as e:
        print(f"Error: {e}")


def display_menu():

    print("\n" + "=" * 50)
    print("  TASK MANAGER  ")
    print("=" * 50)
    print("1. Add new task")
    print("2. View all tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")
    print("=" * 50)


def main():
    """
    Main application loop.
    """
    print("Welcome to Task Manager!")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            add_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            mark_task_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("\nGoodbye! Stay productive!")
            break
        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
