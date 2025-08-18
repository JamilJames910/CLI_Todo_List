import argparse
import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE,'r') as file:
        return json.load(file)
    
def save_tasks(tasks):
    with open(TASKS_FILE,'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    tasks = load_tasks()
    tasks.append({'description': description, 'done':False})
    save_tasks(tasks)
    print(f"✅ Task added: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks: 
        print("📭 No tasks found.")
        return 
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task ["done"] else "🕒"
        print(f"{i}. {status} {task['description']}")

def complete_task(index):
    tasks = load_tasks()
    try: 
        tasks[index - 1]['done'] = True
        save_tasks(tasks)
        print(f"✅ Task #{index} marked as done.")
    except IndexError:
        print("❌ Invalid task number.")

def delete_task(index): 
    tasks = load_tasks()
    try: 
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️ Task deleted: {removed['description']}")
    except IndexError:
        print("❌ Invalid task number.") 

def main():
    parser = argparse.ArgumentParser(description="📝 Simple CLI To-Do List")
    subparsers = parser.add_subparsers(dest='command')

    # Add Command 
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', type=str, help='Task description')
        
    # List Command
    subparsers.add_parser('list', help='List all tasks') 

    # Complete Command 
    complete_parser = subparsers.add_parser('done', help='Mark task as complete')
    complete_parser.add_argument('index', type=int, help='Task number to mark as done')

    # Delete Command
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('index', type=int, help='Tasks number to delete')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'list': 
        list_tasks()
    elif args.command == 'done': 
        complete_task(args.index)
    elif args.command == 'delete':
        delete_task(args.index)
    else: 
        parser.print_help()

if __name__ == '__main__':
    main()
