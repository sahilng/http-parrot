from flask import Flask, Response
import os

app = Flask(__name__)

PORT = int(os.environ.get('PORT', 5000))  # Ensure PORT is cast to int
SAY = os.environ.get('SAY', 'Hello, set the SAY environment variable to receive a parroted response!')

@app.route("/")
def hello_world():
    # Add a newline character at the end of the response
    return Response(f"{SAY}\n", mimetype='text/plain')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
