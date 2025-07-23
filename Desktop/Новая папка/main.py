from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Fake database
todos = []

class Todo(BaseModel):
    title: str
    completed: bool = False

@app.get("/")
def home():
    return {"message": "Todo List API ishlayapti!"}

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo qo‘shildi", "todo": todo}

@app.put("/todos/{index}")
def update_todo(index: int, todo: Todo):
    if index >= len(todos):
        raise HTTPException(status_code=404, detail="Todo topilmadi")
    todos[index] = todo
    return {"message": "Todo yangilandi", "todo": todo}

@app.delete("/todos/{index}")
def delete_todo(index: int):
    if index >= len(todos):
        raise HTTPException(status_code=404, detail="Todo topilmadi")
    deleted = todos.pop(index)
    return {"message": "Todo o‘chirildi", "todo": deleted}
