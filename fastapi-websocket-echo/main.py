"""
pip install fastapi uvicorn websockets
uvicorn main:app --reload


"""

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse


html_body = """
<!DOCTYPE html>
<html>
<head>
    <title>WebSocket Test</title>
</head>
<body>
    <h2>WebSocket Echo Test</h2>

    <input id="messageInput" type="text" placeholder="Enter message">
    <button onclick="sendMessage()">Send</button>

    <h3>Messages</h3>
    <ul id="messages"></ul>

    <script>
        const ws = new WebSocket("ws://localhost:8000/ws");

        ws.onmessage = function(event) {
            const li = document.createElement("li");
            li.textContent = event.data;
            document.getElementById("messages").appendChild(li);
        };

        function sendMessage() {
            const input = document.getElementById("messageInput");
            ws.send(input.value);
            input.value = "";
        }
    </script>
</body>
</html>
"""


app = FastAPI()


@app.websocket("/ws")
async def chat_echo_server(web_socket: WebSocket):
    try:
        await web_socket.accept()
        while True:
            user_input = await web_socket.receive_text()
            await web_socket.send_text(f"Server received: {user_input}")
    except WebSocketDisconnect as error:
        print(f"Client disconnected:")


@app.get("/")
async def home():
    return HTMLResponse(html_body)
