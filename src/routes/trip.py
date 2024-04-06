from flask import Blueprint, request, make_response, jsonify
from middlewares.token_verification import token_required
from genai.prompt import suggest_trip

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
	return make_response(jsonify(returnJson), 200)