# Splitgate API
Proxy server for Tracker GGs Split Gate API

The server can be found running [here](https://splitgate-api.onrender.com/).

## Usage
The server currently takes two URL parameters 'platform' and 'username'.

Platform can be anyone of 'steam', 'xbl' or 'psn' which correspond to Steam/PC, Xbox Live and PlayStation respectively.

Username is the username of your account on that platform: SteamID64 for Steam/PC, Xbox Gamertag for Xbox Live and PSN Id for PlayStation.

For example, to access LJRex's Splitgate stats on Steam, you would access the endpoint `https://splitgate-api.onrender.com/?platform=steam&username=76561198059390699`.
