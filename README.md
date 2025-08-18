# 📝 CLI To-Do List

A simple, lightweight, and user-friendly command-line interface (CLI) To-Do List application built with Python. This tool allows you to efficiently manage tasks directly from your terminal, providing features to add, list, complete, and delete tasks.

---

## Table of Contents

- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Example](#example)  
- [File Structure](#file-structure)  
- [Technical Details](#technical-details)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Features

- **Add Tasks:** Quickly add tasks with descriptions.  
- **List Tasks:** Display all tasks with their current status (pending or completed).  
- **Complete Tasks:** Mark tasks as completed to track progress.  
- **Delete Tasks:** Remove tasks that are no longer relevant.  
- **Persistent Storage:** Tasks are saved in a `tasks.json` file, ensuring your data is retained between sessions.  
- **Intuitive CLI:** Easy-to-use commands and clear visual indicators using emojis for better user experience.

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/cli-todo-list.git
cd cli-todo-list
````

2. **Ensure Python 3.7+ is installed**

Check your Python version:

```bash
python --version
```

3. **Install dependencies (if any)**

This project uses only standard Python libraries (`argparse`, `json`, `os`), so no additional dependencies are required.

---

## Usage

The CLI provides four main commands: `add`, `list`, `done`, and `delete`.

### Add a Task

```bash
python todo.py add "Finish writing README"
```

Adds a new task to your list.

### List All Tasks

```bash
python todo.py list
```

Displays all tasks with their status:

* 🕒 Pending
* ✅ Completed

### Complete a Task

```bash
python todo.py done 1
```

Marks the task with the given index as completed.

### Delete a Task

```bash
python todo.py delete 2
```

Removes the task with the given index from your list.

---

## Example

```bash
$ python todo.py add "Finish Python project"
✅ Task added: Finish Python project

$ python todo.py list
1. 🕒 Finish Python project

$ python todo.py done 1
✅ Task #1 marked as done.

$ python todo.py list
1. ✅ Finish Python project

$ python todo.py delete 1
🗑️ Task deleted: Finish Python project
```

---

## File Structure

```
cli-todo-list/
├── todo.py          # Main Python CLI script
├── tasks.json       # JSON file storing tasks
└── README.md        # Project documentation
```

---

## Technical Details

* **Language:** Python 3
* **Data Storage:** JSON file (`tasks.json`) for persistence
* **Libraries Used:** `argparse`, `json`, `os`
* **Design Approach:**

  * Modular functions for each feature (add, list, complete, delete)
  * Error handling for invalid input
  * Emoji-based status indicators for user-friendly visualization

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -m "Add feature"`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Open a Pull Request

---


> Crafted with ❤️ for developers who love simplicity and productivity in the terminal.


