"""
pip install fastapi uvicorn websockets
uvicorn main:app --reload


"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()


@app.websocket("/ws")
async def chat_echo_server(web_socket: WebSocket):
    try:
        print("WS service called")
        await web_socket.accept()
        print("Web socket connection is accepted")
        user_input = await web_socket.receive_text()
        await web_socket.send_text(f"Server received: {user_input}")
    except Exception as error:
        print(f"Client disconnected: {error}")
