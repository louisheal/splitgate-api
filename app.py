from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

url = 'https://public-api.tracker.gg/v2/splitgate/standard/profile'
platform = 'steam'
username = '76561198059390699'
header = {"TRN-Api-Key":os.getenv("api_key")}

@app.route('/')
def home():
    response = requests.get(url + '/' + platform + '/' + username, headers = header)
    response = jsonify(response.json())
    return response
