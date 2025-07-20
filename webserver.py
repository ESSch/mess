import json
from sys import argv
from flask import Flask, request, render_template

# cd ~/Documents/chatbot/messagers/werryxgamesMessenger/Messenger/
# pip3 install -r requirements.txt
# python webserver.py

print("Program start.");

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(port=8000)