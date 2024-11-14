from flask import Flask
import os

app = Flask(__name__)

PORT = os.environ.get('PORT', 5000)
SAY = os.environ.get('SAY', 'Hello, set the SAY environment variable to receive a parroted response!')

@app.route("/")
def hello_world():
    return SAY

app.run(host='0.0.0.0', port = PORT)