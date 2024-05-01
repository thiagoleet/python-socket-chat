from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)



@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@socketio.on('message')
def handle_message(message):
    print(f"A new message: {message}")
    socketio.emit('message', message)

if __name__ == '__main__':
    socketio.run(app=app, debug=True, port=3000, allow_unsafe_werkzeug=True)