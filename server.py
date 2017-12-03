from flask import Flask
from flask import request
import api

app = Flask(__name__)

@app.route("/api/set", methods=['POST', 'GET'])
def set():
    return api.success()
