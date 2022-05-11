import flask
from flask import Flask, request


app = Flask(__name__)
users = []


@app.route('/user', methods=['GET'])
def get_user():
	return flask.jsonify(users)


@app.route('/user', methods=['POST'])
def create_user():
	data = request.json
	if 'name' in data and 'lastname' in data and 'password' in data and 'email' in data:
		email = data['email']
		if len(list(filter(lambda x: x['email'] == email, users))) != 0:
			return flask.jsonify({
					'code': 2,
					'message': 'Пользователь уже есть в системе'
			})
		users.append(data)
		return flask.jsonify({
			'code': 0,
			'message': 'User created'
		})
	return flask.jsonify({
			'code': 1,
			'message': 'У пользователя есть обязательные поля: name, lastname, password, email'
	})


@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id: int):
	global users
	if len(users) >= user_id:
		users.pop(user_id - 1)
		return flask.jsonify({
			'code': 0,
			'message': 'User deleted!'
		})
	return flask.jsonify({
			'code': 3,
			'message': 'User not found!'
		})


if __name__ == '__main__':
	app.run(debug=True)

