from fastapi import FastAPI, BackgroundTasks
import time

app = FastAPI()


def back_ground_task(message: str):
    print("back_ground_task started")
    time.sleep(10)
    print(f"sent message {message}")
    print("back_ground_task ends")


def back_ground_task1(message: str):
    print("back_ground_task1 started")
    time.sleep(10)
    print(f"sent message {message}")
    print("back_ground_task1 ends")


def back_ground_task2(message: str):
    print("back_ground_task2 started")
    time.sleep(10)
    print(f"sent message {message}")
    print("back_ground_task2 ends")


def back_ground_task3(message: str, timer_value: int):
    print("back_ground_task2 started")
    time.sleep(timer_value)
    print(f"sent message {message}")
    print("back_ground_task2 ends")


@app.get("/order")
def place_order(background_task: BackgroundTasks):
    print("order URI is called")
    background_task.add_task(back_ground_task, "order placed successfully")
    background_task.add_task(back_ground_task1, "seller notified successfully")
    background_task.add_task(back_ground_task2, "seller acknowledged successfully")
    background_task.add_task(back_ground_task2, "seller confirmed shipping")
    background_task.add_task(back_ground_task3, "seller shared tracking", 20)
    print("User is respondeded while other background tasks are going on")
    return {"place_order": "responded"}
