# CLI Task Manager

A lightweight command-line task manager written in Python. Add tasks, organize them by priority, update their status, and keep your list between runs with local JSON storage.

## Features

- Add tasks with high, medium, or low priority
- View tasks ordered by priority
- Mark tasks as completed
- Edit task names or delete tasks
- Save and load tasks using `tasks.json`
- Validate task names, menu choices, and task IDs

## Requirements

- Python 3
- No third-party packages required

## Run

Open a terminal in the project folder and run:

```bash
python main.py
```

On Windows, you can also use:

```powershell
py main.py
```

Choose an option from the menu and follow the prompts. Tasks are saved in `tasks.json` in the current project folder when changes are made and when you exit. If the file does not exist yet, it is created the first time tasks are saved.

## Project files

| File | Purpose |
| --- | --- |
| `main.py` | Displays the menu and coordinates task operations |
| `task.py` | Adds, completes, edits, and deletes tasks |
| `storage.py` | Loads tasks from and saves tasks to JSON |
| `tasks.json` | Local task data, created as needed and excluded from Git |

## Task data

Each task is stored with an ID, name, priority, and status. Task data stays local in `tasks.json`; that file is ignored by Git so your personal task list is not included when the project is pushed to a repository.