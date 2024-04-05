from flask import Blueprint
from urllib.parse import urlencode
import os

blueprint = Blueprint('auth', __name__)

@blueprint.route('/login')
def signup():
	params = {
		"response_type": "token",
		"client_id": os.environ.get('AUTH0_CLIENT_ID'),
		"redirect_uri": os.environ.get('AUTH0_REDIRECT_URI'),
		"scope": "openid profile email"
	}

	domain = os.environ.get('AUTH0_DOMAIN')
	return { "url": f'https://{domain}/authorize?{urlencode(params)}' }