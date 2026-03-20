from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse, StreamingResponse
import time

app = FastAPI()


html_code = html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.websocket("/ws")
async def ws_service(web_socket: WebSocket):
    try:
        print("inside WS service")
        ws_conn_obj = await web_socket.accept()
        print("WS request is accepted")
        while True:
            user_request = await web_socket.receive_text()
            response = f"Server responded: {user_request}"
            await web_socket.send_text(response)
    except WebSocketDisconnect:
        print("Webscoket is discontinued")


@app.get("/ws_request")
async def user_input_request():
    return HTMLResponse(html_code)

