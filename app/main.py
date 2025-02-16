from fastapi import FastAPI
from app.routers.task import router as task_router
from app.routers.user import router as user_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task_router)
app.include_router(user_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)








