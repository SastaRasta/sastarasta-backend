from flask import Blueprint, request
import requests
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

@blueprint.route('/details')
def details():
	if "Authorization" in request.headers:
		token = request.headers["Authorization"].split(" ")[1]
	if not token:
		return {
			"message": "Authentication Token is missing!",
			"data": None,
			"error": "Unauthorized"
		}, 401
	res = requests.get(f'https://{os.environ.get("AUTH0_DOMAIN")}/userinfo', headers={
		"Authorization": f'Bearer {token}'
	})

	if res.status_code != 200:
		return {
			"message": "Invalid Token",
			"data": None,
			"error": "Unauthorized"
		}, 401
			
	user_info = res.json()
	return user_info
