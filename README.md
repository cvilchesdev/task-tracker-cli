# Task Tracker CLI

CLI simple para gestionar tareas (to-do list) desde la terminal. Permite crear, listar, actualizar, cambiar estado y eliminar tareas.  
Las tareas se guardan en un archivo `tasks.json` en el directorio actual (persistencia en disco).

## Requisitos

- Python 3.10+ (recomendado 3.11+)
- No usa librerías externas (solo estándar)

## Instalación

Clona o descarga el proyecto y entra a la carpeta:

```bash
cd task-tracker-CLI
```

## Para usar:

```bash
python3 task_cli.py <comando> [argumentos]
```

## Para ver la ayuda:

```bash
python3 task_cli.py help
```

## Comandos:

### Agregar tareas:

```bash
python3 task_cli.py add "Comprar pan"
```

### Listar

#### Todas:

```bash
python3 task_cli.py list
```

#### por estado:

```bash
python3 task_cli.py list to-do
python3 task_cli.py list in-progress
python3 task_cli.py list done
```

### Actualizacion:

```bash
python3 task_cli.py update 1 "Comprar pan y leche"
```

### Marcar estado:

#### in-progress:

```bash
python3 task_cli.py mark-in-progress 1
```

#### done:

```bash
python3 task_cli.py mark-done 1
```

### Eliminar

```bash
python3 task_cli.py delete 1
```

## Persistencia (tasks.json):

El archivo tasks.json se crea automáticamente si no existe. Estructura:

```json
[
  {
    "id": 1,
    "description": "Comprar pan",
    "status": "to-do",
    "createdAt": "2026-01-04T15:20",
    "updatedAt": "2026-01-04T15:20"
  }
]
```

## Manejo de errores:

- Si falta un argumento, el programa muestra el Uso: correspondiente.
- Si el id no es numérico, muestra un mensaje de uso.
- Si el id no existe, informa el error y no modifica el archivo.

## Estructura del proyecto:

- task_cli.py : código del CLI y lógica de persistencia
- tasks.json : base de datos local (se genera automáticamente)
