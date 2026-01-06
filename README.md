# Todo App (Python)

A console-based Todo application built using OOP and JSON persistence.

## Features
- Add a todo
- List all todos
- Mark a todo as completed
- Data persists across runs using `todos.json`

## Project Structure
- `main.py` - entry point (menu + user input)
- `manager.py` - manages todos (business logic)
- `todo.py` - Todo model (state + behavior)
- `storage.py` - save/load to JSON

## How to Run
```bash
python main.py
