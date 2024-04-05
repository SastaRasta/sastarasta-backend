# Trip Trekker

## Index
1. [Project setup](#project-setup)
2. [Project structure](#project-structure)
3. [Example to create a new route](#example-to-create-a-new-route)
4. [Custom VSCode Snippets](#custom-vscode-snippets)


## Project setup

1. Clone the repository `$ git clone`
2. Change directory to the project folder `$ cd`
3. Create a virtual environment using your preferred tool (virtualenv, conda, etc.)
4. Install the project dependencies `$ pip install -r requirements.txt`
5. Fill in the environment variables in a `.env` file. You can use the `.env.example` file as a template.
6. Run the server for development `$ python src/main.py`

> **Note:** The project assumes that the the python comand is executed from root of the project. Please refrain from running the project from any other directory.

## Project structure
1. `src/` - Contains the all source code of the project
2. `src/routes` - Contains the routes to handle different requests
	- Please follow the below mentioned syntax to create a new route

## Example to create a new route
Lets say you want to create a new route for authentication. You can create a new file inside the `src/routes` directory with the name `auth.py`. The directory structure will look like this:
```
src/
  - routes/
    - auth.py
```

and lets say you want to create two routes inside the `auth.py` file, one for login and one for logout. The file will look like this:
```python
from flask import Blueprint, request, jsonify

blueprint = Blueprint('auth', __name__)

@blueprint.route('/login', methods=['POST'])
def login():
	return jsonify({'message': 'Login successful'})

@blueprint.route('/logout', methods=['POST'])
def login():
	return jsonify({'message': 'Logout successful'})
```

Now, to access the login route, you can use the following URL:
`http://localhost:5000/auth/login` and similarly, for logout route, you can use the following URL:
`http://localhost:5000/auth/logout`

> **Note:** The project automatically registers the blueprints and routes with the flask app. All you need to do is create a new file inside the `src/routes` directory and follow the syntax as mentioned above.

## Custom VSCode Snippets
To use these custom snippets, just type the snippet in the editor and press `tab` to expand the snippet.

| Snippet | Description |
| ------- | ----------- |
|`bp`|Generates a blueprint template for files inside `src/routes` directory|
|`bpr`|Generates a route function with decorator attached|
|`bprg`|Generates a route function with GET method|
|`bprp`|Generates a route function with POST method|