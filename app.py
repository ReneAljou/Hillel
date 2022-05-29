import flask
from flask import Flask, request


app = Flask(__name__)
projects = []


@app.route('/project', methods=['GET'])
def get_project():
	return flask.jsonify(projects)


@app.route('/project', methods=['POST'])
def create_project():
	data = request.json
	if 'name' in data and 'description' in data and 'deadline' in data and 'creaturedate' in data:
		return flask.jsonify({
			'code': 0,
			'message': 'Проект создан!'
		})
	return flask.jsonify({
			'code': 1,
			'message': 'У проекта есть обязательные поля: name, description, deadline, creaturedate'
	})


@app.route('/project/<int:project_id>', methods=['PUT'])
def update_project(project_id: int):

	data = request.json
	if len(projects) >= project_id:
		if 'name' in data and 'description' in data and 'deadline' in data and 'creaturedate' in data:
			projects[project_id - 1] = data
			return flask.jsonify({
				'code': 0,
				'message': 'Проект обновлён'
			})
		return flask.jsonify({
			'code': 1,
			'message': 'У проекта есть обязательные поля: name, description, deadline, creaturedate'
		})
	return flask.jsonify({
			'code': 3,
			'message': 'Проект не найден!'
		})


@app.route('/project/<int:project_id>', methods=['DELETE'])
def delete_project(project_id: int):
	global projects
	if len(projects) >= project_id:
		projects.pop(project_id - 1)
		return flask.jsonify({
			'code': 0,
			'message': 'Проект удален'
		})
	return flask.jsonify({
			'code': 3,
			'message': 'Проект не найден'
		})


if __name__ == '__main__':
	app.run(debug=True)

