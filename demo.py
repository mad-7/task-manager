#!/usr/bin/env python3

from tasks import (
    add_task, list_tasks, mark_task_done, 
    load_tasks, save_tasks, TASKS_FILE
)
import json

def demo():
    """Demonstrate the task manager functionality"""
    
    print("=" * 60)
    print("TASK MANAGER DEMONSTRATION")
    print("=" * 60)
    
    # Show initial tasks
    print("\n1. VIEWING CURRENT TASKS:")
    print("-" * 60)
    list_tasks()
    
    # Simulate showing file contents
    print("\n\n2. TASKS.JSON FILE CONTENT:")
    print("-" * 60)
    with open(TASKS_FILE, 'r') as f:
        content = f.read()
        print(content)
    
    # Show statistics
    print("\n3. TASK STATISTICS:")
    print("-" * 60)
    tasks = load_tasks()
    pending = sum(1 for t in tasks if t['status'] == 'pending')
    done = sum(1 for t in tasks if t['status'] == 'done')
    
    print(f"Total tasks: {len(tasks)}")
    print(f"Pending: {pending}")
    print(f"Completed: {done}")
    print(f"Completion rate: {(done/len(tasks)*100):.1f}%" if tasks else "N/A")
    
    print("\n" + "=" * 60)
    print("DEMONSTRATION COMPLETE")
    print("=" * 60)
    print("\nTo run the interactive application, use:")
    print("  python3 tasks.py")

if __name__ == "__main__":
    demo()
