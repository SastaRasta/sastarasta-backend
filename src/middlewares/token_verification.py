from functools import wraps
from flask import request
import requests
import os

def token_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		token = None
		if "Authorization" in request.headers:
			token = request.headers["Authorization"].split(" ")[1]
		if not token:
			return {
				"message": "Authentication Token is missing!",
				"data": None,
				"error": "Unauthorized"
			}, 401
		try:
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

		except Exception as e:
			return {
				"message": "Something went wrong",
				"data": None,
				"error": str(e)
			}, 500

		return f(user_info, *args, **kwargs)

	return decorated