from fastapi import FastAPI, Path
import time
import asyncio

test_app = FastAPI()


@test_app.get("/syncapi/{app_id}")
def test_sync_api(app_id=Path(...)):
    print(f"Entry {app_id}")
    time.sleep(10)
    print(f"exit {app_id}")
    return {"Message": "hello"}


@test_app.get("/asyncapi/{app_id}")
async def test_sync_api(app_id=Path(...)):
    print(f"Entry {app_id}")
    asyncio.sleep(10)
    print(f"exit {app_id}")
    return {"Message": "hello1"}
