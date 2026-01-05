
from todo import ToDo
from storage import save_todos, load_todos

class ToDoManager():
    def __init__(self):
        self.todo_list = load_todos()
    
    def add_todo(self, title):
        todo = ToDo(title)
        self.todo_list.append(todo)
        save_todos(self.todo_list)
    
    def list_all_todos(self):
        for index, todo in enumerate(self.todo_list):
            status = "Done" if todo.completed else "not done yet"
            print(f"{index}. {todo.title} {status}")
    
    def mark_done(self, index):
        if 0 <= index < len(self.todo_list):
            self.todo_list[index].mark_done()
            save_todos(self.todo_list)
        else:
            print("Invalid Index Value")