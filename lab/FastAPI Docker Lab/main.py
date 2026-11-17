from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI Application"}

@app.get("/about")
def about():
    return {"message": "This is my FastAPI lab application"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}