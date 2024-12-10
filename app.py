from flask import Flask, request, redirect, url_for
import os, traceback, requests

app = Flask(__name__)

#ENVIRONMENT VARIABLES
CLIENT_ID     = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
REDIRECT_URI  = os.environ['REDIRECT_URI']
DISCORD_API_BASE_URL = os.environ['DISCORD_API_BASE_URL']


# Route for the root endpoint with GET method
@app.route('/', methods=['GET'])
def home():
    return "<h1><a href='DISCORD-GENERATED URL'>Login into Discord</a></h1>"
    
@app.route( "/redirect", methods=['GET', 'POST'] )
def redirect():
    code = request.args.get('code')
    msg = ""

    msg += f"Code received: {code}<BR/><BR/>"

    # Exchange code for access token
    token_data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI
    }
    
    msg += "Get the Access Token<BR/><BR/>"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    token_response = requests.post(f"{DISCORD_API_BASE_URL}/oauth2/token", data=token_data, headers=headers)
    token_json = token_response.json()
    access_token = token_json['access_token']
    msg += f"Access Token retrieved: {access_token}<BR/><BR/>"

    # Step 6: Fetch User Information
    user_headers = {'Authorization': f'Bearer {access_token}'}
    user_response = requests.get(f"{DISCORD_API_BASE_URL}/users/@me", headers=user_headers)
    user_info = user_response.json()

    msg += f"<BR/>User Info: {user_info}<BR/><BR/>"

    return msg

if __name__ == '__main__':
    app.run(host='localhost', port=5000)    
