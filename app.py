from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

url = 'https://public-api.tracker.gg/v2/splitgate/standard/profile'
header = {"TRN-Api-Key":os.getenv("api_key")}

@app.route('/')
def home():
    args = request.args
    if "platform" in args:
        if "username" in args:
            response = requests.get(url + '/' + args.get("platform") + '/' + args.get("username"), headers = header)
            return response
        else:
            return "Argument \"username\" not set", 400
    else:
        return "Argument \"platform\" not set", 400
