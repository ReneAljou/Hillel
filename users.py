from flask import Flask

app = Flask(__name__)

"""
https://code.visualstudio.com/docs/supporting/faq - ссылка

https - протокол
code.visualstudio.com - домен
/docs/supporting/faq - путь (route)
"""


@app.route('/')
def home_page():
	with open('html/index.html', 'r') as f:
		return f.read()


ALL_USERS = [
	{
		'id': 1,
		'name': 'John',
		'description': 'He is a man'
	},
	{
		'id': 2,
		'name': 'Kevin',
		'description': 'He is a man'
	},
	{
		'id': 3,
		'name': 'Jack',
		'description': 'He is a man'
	}
]

@app.route('/users')
def all_users():
	response = ''
	for user in ALL_USERS:
		response += f'<a href="/user/{user["id"]}"><h1>{user["name"]}</p>'
	return response


@app.route('/user/<int:id>')
def get_user(id: int):
	for user in ALL_USERS:
		if user['id'] == id:
			return f'<h1>{user["name"]}</h1><p>{user["description"]}</p>'
	return '<p style="color:red;">User not found</p>'

app.run('localhost', 8000)


"""
Задание:
Создать глобальную переменную ALL_USERS в которую поместить 4 пользователя
Нужно написать два запроса /users и /user/<id>
Первый запрос должен возвращать список всех пользователей
Второй запрос должен возвращать пользователя с заданным id
"""
