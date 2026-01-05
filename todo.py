class ToDo():
    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_done(self):
        self.completed = True

    def to_dict(self):
        return {"title":self.title, "completed":self.completed}
    
    def from_dict(data):
        todo = ToDo(data["title"])
        todo.completed = data["completed"]
        return todo

