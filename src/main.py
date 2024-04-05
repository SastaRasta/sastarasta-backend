from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv, find_dotenv
from routes import load_routes
import os
from authlib.integrations.flask_client import OAuth

load_dotenv(find_dotenv('../.env'))
app = Flask(__name__)
CORS(app)
load_routes(app)
oauth = OAuth(app)

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('APP_PORT')) or 5000)
