# Task Tracker CLI

A simple CLI to manage tasks (to-do list) from the terminal. It allows you to create, list, update, change status, and delete tasks.
Tasks are stored in a tasks.json file in the current directory (disk persistence).

## Requirements

- Python 3.10+ (3.11+ recommended)
- No external libraries used (standard library only)

## Installation

Clone or download the project and enter the folder:

```bash
cd task-tracker-CLI
```

## Usage:

```bash
python3 task_cli.py <command> [arguments]
```

## Show help:

```bash
python3 task_cli.py help
```

## Commands:

### Add tasks:

```bash
python3 task_cli.py add "Buy bread"
```

### List

#### All:

```bash
python3 task_cli.py list
```

#### By status:

```bash
python3 task_cli.py list to-do
python3 task_cli.py list in-progress
python3 task_cli.py list done
```

### Update:

```bash
python3 task_cli.py update 1 "Buy bread and milk"
```

### Change status

#### in-progress:

```bash
python3 task_cli.py mark-in-progress 1
```

#### done:

```bash
python3 task_cli.py mark-done 1
```

### Delete

```bash
python3 task_cli.py delete 1
```

## Persistence (tasks.json):

The tasks.json file is automatically created if it does not exist. Structure:

```json
[
  {
    "id": 1,
    "description": "Buy bread",
    "status": "to-do",
    "createdAt": "2026-01-04T15:20",
    "updatedAt": "2026-01-04T15:20"
  }
]
```

## Error handling:

- If an argument is missing, the program displays the corresponding usage message.
- If the id is not numeric, a usage message is shown.
- If the id does not exist, the error is reported and the file is not modified.

## Project structure:

- task_cli.py : CLI code and persistence logic
- tasks.json : local database (auto-generated)
