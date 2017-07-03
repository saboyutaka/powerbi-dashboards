import os, requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index(name=None):
    
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
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)