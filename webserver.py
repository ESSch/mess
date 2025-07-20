import json
from sys import argv
from flask import Flask, request, render_template
from flask_socketio import SocketIO, send, emit, join_room, leave_room

# cd ~/Documents/chatbot/messagers/werryxgamesMessenger/Messenger/
# pip3 install -r requirements.txt
# python webserver.py

print("Program start.");
users = {}

app = Flask(__name__)
socketio = SocketIO(app)

# for test: curl -X GET http://localhost:8000/hello
# response: Hello, world!
@app.route('/hello', methods=['GET'])
def hello_get():
    name = request.args.get('name', 'world')
    return f"Hello, {name}!"

@app.route('/login', methods=['GET'])
def login_get():
    return render_template('login.html')

@app.route('/', methods=['GET'])
def main_get():
    my_list = ["Item 1", "Item 2", "Item 3", "Another Item"]
    return render_template('index.html', items=my_list)

# Handle new user joining
@socketio.on('join')
def handle_join(username):
    users[request.sid] = username  # Store username by session ID
    join_room(username)  # Each user gets their own "room"
    emit("message", f"{username} joined the chat", room=username)

# Handle user messages
@socketio.on('message')
def handle_message(data):
    username = users.get(request.sid, "Anonymous")  # Get the user's name
    emit("message", f"{username}: {data}", broadcast=True)  # Send to everyone

# Handle disconnects
@socketio.on('disconnect')
def handle_disconnect():
    username = users.pop(request.sid, "Anonymous")
    emit("message", f"{username} left the chat", broadcast=True)

if __name__ == '__main__':
    socketio.run(app, port=8000, debug=True)