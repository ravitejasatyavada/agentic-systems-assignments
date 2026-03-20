from fastapi import FastAPI, BackgroundTasks
import time

app = FastAPI()


def bg_task(message: str):
    time.sleep(2)
    print(f"{message} completed")


@app.get("/order")
def background_tasks(bg_tasks: BackgroundTasks):
    print("Background task initiated")
    print(bg_tasks.add_task(bg_task, "order placed"))
    print(bg_tasks.add_task(bg_task, "order ack"))
    print(bg_tasks.add_task(bg_task, "seller shipped"))
    return {"message": "user response"}
