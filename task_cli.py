import sys
import json
import os
from datetime import datetime


def main(argv: list[str]) -> None:
    if len(argv) < 2:
        print("Uso: task-cli <comando> [argumentos]")
        return

    command = argv[1]

    if command in {"help", "-h", "--help"}:
        print_help()
        return

    if command == "add":
        if len(argv) < 3:
            print('Uso: task-cli add "descripcion"')
            return

        task_id = add_task(argv[2])

        if task_id is None:
            print('Uso: task-cli add "descripcion"')
            return

        print(f"Tarea agregada exitosamente (ID: {task_id})")

    elif command == "update":
        if len(argv) < 4:
            print('Uso: task-cli update <id> "descripcion"')
            return

        try:
            task_id = int(argv[2])
        except ValueError:
            print('Uso: task-cli update <id> "descripcion" (id debe ser numerico)')
            return

        new_description = argv[3].strip()
        if not new_description:
            print('Uso: task-cli update <id> "descripcion"')
            return

        if update_task(task_id, new_description):
            print(f"Tarea actualizada exitosamente (ID: {task_id})")
        else:
            print(f"Error: no existe una tarea con ID {task_id}")

    elif command == "delete":
        if len(argv) < 3:
            print("Uso: task-cli delete <id>")
            return

        try:
            task_id = int(argv[2])
        except ValueError:
            print("Uso: task-cli delete <id> (id debe ser un numero)")
            return

        if delete_task(task_id):
            print(f"Tarea eliminada exitosamente (ID: {task_id})")
        else:
            print(f"Error: no existe una tarea con ID {task_id}")

    elif command == "mark-in-progress":
        if len(argv) < 3:
            print("Uso: task-cli mark-in-progress <id>")
            return

        try:
            task_id = int(argv[2])
        except ValueError:
            print("Uso: task-cli mark-in-progress <id> (id debe ser numerico)")
            return

        if mark_task(task_id, "in-progress"):
            print(f"Tarea {task_id} marcada como in-progress")
        else:
            print(f"Error: no existe una tarea con ID {task_id}")

    elif command == "mark-done":
        if len(argv) < 3:
            print("Uso: task-cli mark-done <id>")
            return

        try:
            task_id = int(argv[2])
        except ValueError:
            print("Uso: task-cli mark-done <id> (id debe ser numerico)")
            return

        if mark_task(task_id, "done"):
            print(f"Tarea {task_id} marcada como done")
        else:
            print(f"Error: no existe una tarea con ID {task_id}")

    elif command == "list":
        tasks = load_tasks()

        # filtro opcional
        status_filter = None
        if len(argv) >= 3:
            status_filter = argv[2]

        # validar filtro si viene
        valid_status = {"to-do", "in-progress", "done"}
        if status_filter is not None and status_filter not in valid_status:
            print('Uso: task-cli list [to-do|in-progress|done]')
            return

        # filtrar si corresponde
        for t in tasks:
            if status_filter is None or t["status"] == status_filter:
                print(f'[{t["id"]}] ({t["status"]}) {t["description"]}')

    else:
        print(f"Comando desconocido: {command}")


TASK_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []

    with open(TASK_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def add_task(description: str) -> int | None:
    description = description.strip()
    if not description:
        return None

    tasks = load_tasks()

    # calcular nuevo id (max + 1)
    if tasks:
        new_id = max(t["id"] for t in tasks) + 1
    else:
        new_id = 1

    now = datetime.now().isoformat(timespec="minutes")

    task = {
        "id": new_id,
        "description": description,
        "status": "to-do",
        "createdAt": now,
        "updatedAt": now,
    }

    tasks.append(task)
    save_tasks(tasks)
    return new_id


def mark_task(task_id: int, new_status: str) -> bool:
    tasks = load_tasks()
    now = datetime.now().isoformat(timespec="minutes")

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updatedAt"] = now
            save_tasks(tasks)
            return True
    return False


def delete_task(task_id: int) -> bool:
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]

    if len(new_tasks) == len(tasks):
        return False  # no existia

    save_tasks(new_tasks)
    return True


def update_task(task_id: int, new_description: str) -> bool:
    new_description = new_description.strip()
    if not new_description:
        return False

    tasks = load_tasks()
    now = datetime.now().isoformat(timespec="minutes")

    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = now
            save_tasks(tasks)
            return True

    return False


def print_help() -> None:
    print(
        'Uso: task-cli <comando> [argumentos]\n'
        '\n'
        'Comandos:\n'
        '  add "descripcion"                 Agrega una tarea (status: to-do)\n'
        '  update <id> "descripcion"         Cambia la descripción de una tarea\n'
        '  delete <id>                       Elimina una tarea\n'
        '  mark-in-progress <id>             Marca una tarea como in-progress\n'
        '  mark-done <id>                    Marca una tarea como done\n'
        '  list                              Lista todas las tareas\n'
        '  list to-do|in-progress|done       Lista tareas filtrando por estado\n'
        '  help                              Muestra esta ayuda\n'
        '\n'
        'Ejemplos:\n'
        '  task-cli add "Comprar pan"\n'
        '  task-cli update 2 "Comprar pan y leche"\n'
        '  task-cli mark-done 2\n'
        '  task-cli list done\n'
    )


if __name__ == "__main__":
    main(sys.argv)
