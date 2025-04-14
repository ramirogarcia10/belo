from flask import Flask, request
import logging
import os

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/")
def hello():
    user_agent = request.headers.get('User-Agent')
    logging.info(f"[v1] Request from {request.remote_addr} with agent {user_agent}")
    return "Hello from version 1!", 200

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8080))
    app.run(host="0.0.0.0", port=port)