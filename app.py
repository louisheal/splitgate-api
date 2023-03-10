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
        if 'username' in args and validate_username(args.get('username')):
            response = requests.get(url + '/' + args.get('platform') + '/' + args.get('username'), headers = header)
            return response
        else:
            return "Argument \"username\" not set", 400
    else:
        return "Argument \"platform\" not set", 400

"""Splitagte is only available on PC/Steam Xbox and Playstation"""
def validate_platform(platform):
    return platform in ['steam', 'xbl', 'ps4']

"""SteamID64 usernames are only made up of digits"""
def validate_username(username):
    return username.isdigit()
