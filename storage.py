import json
from todo import ToDo

FILE_NAME = "todos.json"

def save_todos(todo_list):
    data = [todo.to_dict() for todo in todo_list]
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=2)

def load_todos():
    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
        return [ToDo.from_dict(item) for item in data]
    except FileNotFoundError:
        return []
