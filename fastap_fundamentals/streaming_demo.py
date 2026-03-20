import time
from fastapi import FastAPI
from fastapi.responses import StreamingResponse


app = FastAPI()


def data_streamer():
    for i in range(100):
        yield f"Value streamed is {i}\n"
        time.sleep(1)


@app.get("/streaming")
async def streaming():
    try:
        return StreamingResponse(data_streamer(), media_type="text/event-streaming")
    except Exception as error:
        print(f"error is {error}")
