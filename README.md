# CLI Todo List 📝

A simple, intuitive, and interactive Python command-line tool to manage your daily tasks.  
Perfect for keeping track of things to do, marking tasks complete, and deleting tasks you’ve finished.

## Features ✨
✅ Add a new task with a description.  
✅ List all tasks with clear status indicators.  
✅ Mark tasks as complete.  
✅ Delete tasks.  
✅ Stores tasks locally in a JSON file.  
✅ Works across different operating systems (Windows, macOS, Linux).  

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Contact](#contact)

## Installation 🛠️
Clone this repository:

```bash
git clone https://github.com/JamilJames910/CLI_Todo_List.git
cd CLI_Todo_List
````

Make sure you have Python 3.x installed.

(Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

No additional dependencies are required—Python's built-in `argparse` and `json` modules handle everything.

## Usage 💻

Run the script:

```bash
python CLI_Todo_List.py
```

You can use the following commands:

* **Add a task:**

```bash
python CLI_Todo_List.py add "Task description"
```

* **List all tasks:**

```bash
python CLI_Todo_List.py list
```

* **Mark a task as done:**

```bash
python CLI_Todo_List.py done 1
```

* **Delete a task:**

```bash
python CLI_Todo_List.py delete 1
```

## Example

```bash
# Add tasks
python CLI_Todo_List.py add "Buy groceries"
python CLI_Todo_List.py add "Clean the house"

# List tasks
python CLI_Todo_List.py list
```

Output:

```
1. 🕒 Buy groceries
2. 🕒 Clean the house
```

```bash
# Complete a task
python CLI_Todo_List.py done 1
```

Output:

```
✅ Task #1 marked as done.
```

```bash
# Delete a task
python CLI_Todo_List.py delete 2
```

Output:

```
🗑️ Task deleted: Clean the house
```

## Project Structure 🗂️

```
CLI_Todo_List
├── CLI_Todo_List.py       # Main script
├── tasks.json             # Local task storage (created automatically)
├── README.md              # Project documentation
└── .gitignore             # Git ignore file
```
## Contributing 🤝

Contributions, suggestions, and improvements are welcome!

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Open a Pull Request.

## Contact ✉️

Created with ❤️ by Jamil James

* GitHub: [JamilJames910](https://github.com/JamilJames910)
* Email: **[Jamil.i.James1@gmail.com](mailto:Jamil.i.James1@gmail.com)**

