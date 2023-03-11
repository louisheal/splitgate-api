from flask import Flask, jsonify, request
import requests
import os

app = Flask(__name__)

url = "https://public-api.tracker.gg/v2/splitgate/standard/profile"
header = {'TRN-Api-Key':os.getenv('api_key')}

@app.route('/')
def home():
    args = request.args

    if 'platform' not in args or invalid_platform(args.get('platform')):
        return "Argument \"platform\" is either missing or incorrect.", 400
    
    if 'username' not in args or invalid_username(str(args.get('username')), args.get('platform')):
        return "Argument \"username\" is either missing or incorrect.", 400

    username, platform = str(args.get('username')), args.get('platform')

    response = requests.get(f"{url}/{platform}/{username}", headers = header)
    return response.json(), 200

def invalid_username(username, platform):
    """WARNING: Always validate the platform first."""
    if platform == 'steam':
        # SteamID64 usernames are only made up of digits
        return not username.isdigit()
    # platform must be 'xbl' or 'psn'
    # Xbox Gamertags and PSN Ids are alphanumeric
    return not username.isalnum()

# Splitagte is only available on Steam/PC, Xbox and PlayStation
def invalid_platform(platform):
    return platform not in ['steam', 'xbl', 'psn']
