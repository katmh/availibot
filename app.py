from flask import Flask
app = Flask(__name__)

@app.route('/availibot', methods=['GET', 'POST'])
def index():
    return 'Hello world!'