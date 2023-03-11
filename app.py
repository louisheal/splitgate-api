from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

url = "https://public-api.tracker.gg/v2/splitgate/standard/profile"
header = {'TRN-Api-Key':os.getenv('api_key')}

@app.route('/')
def home():
    args = request.args
    if 'platform' in args and validate_platform(args.get('platform')):
        platform = args.get('platform')
        if 'username' in args and validate_username(str(args.get('username')), platform):
            username = str(args.get('username'))
            response = requests.get(url + '/' + platform + '/' + username, headers = header)
            return response.json(), 200
        else:
            return "Argument \"username\" not set", 400
    else:
        return "Argument \"platform\" not set", 400

"""Splitagte is only available on PC/Steam Xbox and PlayStation"""
def validate_platform(platform):
    return platform in ['steam', 'xbl', 'psn']

"""SteamID64 usernames are only made up of digits"""
def validate_username(username, platform):
    if platform == 'steam':
        return username.isdigit()
    return username.isalnum()
