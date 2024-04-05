from flask import Flask, url_for, session, redirect
from flask_cors import CORS
from dotenv import load_dotenv, find_dotenv
from routes import load_routes
import os
from authlib.integrations.flask_client import OAuth
from urllib.parse import quote_plus, urlencode

load_dotenv(find_dotenv('../.env'))
app = Flask(__name__)
CORS(app)
load_routes(app)
oauth = OAuth(app)

oauth.register(
    "auth0",
    client_id=os.environ.get("AUTH0_CLIENT_ID"),
    client_secret=os.environ.get("AUTH0_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{os.environ.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
)

@app.route('/signup', methods=['POST'])
def signup():
	return oauth.auth0.authorize_redirect(
        redirect_uri=url_for("callback", _external=True)
    )

@app.route("/callback", methods=["GET", "POST"])
def callback():
    token = oauth.auth0.authorize_access_token()
    session["user"] = token
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('APP_PORT')) or 5000)
