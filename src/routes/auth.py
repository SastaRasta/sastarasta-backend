import os
from supabase import create_client, Client
from flask import Blueprint, url_for

from authlib.integrations.flask_client import OAuth
from urllib.parse import quote_plus, urlencode

blueprint = Blueprint('auth', __name__)


@blueprint.route('/signup', methods=['POST'])
def signup():
	return 'hello'