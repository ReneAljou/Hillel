import flask
from flask import Flask, request

app = Flask(__name__)
users = []

"""
Вопросы:
1) Создание пользователя
"""

"""
Запрос на сервер:
 * путь
 * метод
 * данные
 
 
GET: (Params)
localhost:5000/user?username=Vasya&password=qwerty123&full_name=Vasya Pupkin

POST/PUT/PATCH: (Body)
localhost:5000/user
{
	"username": "Vasya",
	"password": "qwerty123",
	"full_name": "Vasya Pupkin"
}
"""

"""
Задачи: 
* Редактирование пользователя
* Удаление пользователя по id
"""


@app.route('/user', methods=['GET'])
def get_user():
	# request.args  # параметры (params) запроса
	return flask.jsonify(users)


@app.route('/user', methods=['POST'])
def create_user():
	# request.json  # тело запроса (body) запроса
	data = request.json
	if 'username' in data and 'password' in data and 'email' in data:
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
			'message': 'У пользователя есть обязательные поля: username, password, email'
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


@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id: int):
	"""
	username
	password
	email
	"""
	global users
	"""
	data = {
	     "username": "Petya",
	    "password": "qwerty123",
	    "email": "vasya1234567@gmail.com"
	}
	users = [{
	    "username": "Vasya",
	    "password": "qwerty123",
	    "email": "vasya@gmail.com"
	}]
	user = {
	    "username": "Vasya",
	    "password": "qwerty123",
	    "email": "vasya@gmail.com"
	}
	"""
	data = request.json
	if len(users) >= user_id:
		if 'username' in data and 'password' in data and 'email' in data:
			users[user_id - 1] = data
			return flask.jsonify({
				'code': 0,
				'message': 'User updated!'
			})
		return flask.jsonify({
			'code': 1,
			'message': 'У пользователя есть обязательные поля: username, password, email'
		})
	return flask.jsonify({
			'code': 3,
			'message': 'User not found!'
		})


if __name__ == '__main__':
	app.run(debug=True)
