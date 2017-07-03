import os, requests, urllib
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    
    refresh_token = os.getenv('REFRESH_TOKEN')
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')

    dashboard_id = request.args.get('dashboard_id', '')
    
    payload = {
        'grant_type': 'refresh_token', 
        'resource': 'https://analysis.windows.net/powerbi/api',
        'client_id': client_id,
        'client_secret': client_secret,
        'refresh_token': refresh_token
    }
    
    response = requests.post("https://login.microsoftonline.com/common/oauth2/token", data=payload).json()
    return render_template('index.html', dashboard_id=dashboard_id, access_token=response.get('access_token'))
    
@app.route('/authorize', methods=["GET"])
def autorize():
    client_id = os.getenv('CLIENT_ID')
    payload = {
        "response_type": "code",
        "response_mode": "query",
        "resource": "https://analysis.windows.net/powerbi/api",
        "client_id": client_id
    }
    url = "https://login.microsoftonline.com/common/oauth2/authorize?" + urllib.urlencode(payload)
    return redirect(url, code=302)
    
@app.route('/authorize-callback')
def autorize_callback():
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')

    code = request.args.get('code', '')
    
    payload = {
        'grant_type': 'authorization_code', 
        'resource': 'https://analysis.windows.net/powerbi/api',
        'client_id': client_id,
        'client_secret': client_secret,
        'code': code
    }
    
    response = requests.post("https://login.microsoftonline.com/common/oauth2/token", data=payload).json()
    return response.get("refresh_token")
    
application = app

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)