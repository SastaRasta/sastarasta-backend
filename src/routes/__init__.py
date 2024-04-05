import os
import importlib
from flask import Flask

def load_routes(app: Flask) -> None:
	# Import all blueprints
	# the API route will be /<file_name>/<route>
	print(os.getcwd())
	for route in os.listdir('./src/routes'):
		if not route.endswith('.py') \
			or route == '__init__.py':
			continue

		route = route.replace('.py', '')
		module = f'routes.{route}'
		module = importlib.import_module(module)
		app.register_blueprint(module.blueprint, url_prefix=f'/{route}')