from flask import Blueprint, request, make_response, request
from middlewares.token_verification import token_required
from genai.prompt import suggest_trip
from genai.chatbot import get_chatbot_response

blueprint = Blueprint('trip', __name__)

@blueprint.route('/suggest', methods=['POST'])
@token_required
def signup(user_info):
	body = request.json
	params = {
		'start_location': body['start_location'],
		'end_location': body['destination'],
		'budget': body['budget'],
		'start_date': body['from_date'],
		'end_date': body['to_date'],
		'group_size': body['group_size'],
		'extra_information': body['extra_info']
	}

	returnJson = suggest_trip(params)
	print(returnJson)
	
	res = make_response(returnJson['response'])
	res.headers['Content-Type'] = 'text/html'
	res.status_code = 200
	res.mimetype = 'text/html'

	return res

@blueprint.route('/chat')
@token_required
def chat(user_info):
	user_message = request.args.get('message')
	response = get_chatbot_response(user_message)
	return response
