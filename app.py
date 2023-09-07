from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hi This is My first web application,Please subscribe, like, and comment on this video, TY!!!'
