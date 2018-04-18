from flask import Flask, jsonify, abort, make_response, request, url_for
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

app = Flask(__name__)


@auth.get_password
def get_password(username):
    if username == 'k':
        return 'k'
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


# 修改404页面返回json数据
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}))


@app.route('/')
def index():
    return "Learn Flask-Restful!"


tasks = [{
    'id': 1,
    'title': u'Buy groceries',
    'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
    'done': False
}, {
    'id': 2,
    'title': u'Learn Python',
    'description': u'Need to find a good Python tutorial on the web',
    'done': False
}]


# 把ids处理成uri
def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for(
                'get_task', task_id=task['id'], _external=True)
        else:
            new_task[field] = task[field]
    return new_task


# 返回所有task
@app.route('/todo/api/v1.0/tasks', methods=["GET"])
@auth.login_required
def get_tasks():
    return jsonify({'tasks': [make_public_task(t) for t in tasks]})
    # py3:map()生成的是map对象,不是list,不能作为jsonify参数


# 返回指定id的task
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=["GET"])
def get_task(task_id):
    task = [t for t in tasks if t['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


# 添加一个task
@app.route('/todo/api/v1.0/tasks', methods=["POST"])
def create_task():
    if not request.json and not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'desciption': request.json.get('desciption', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


# 修改task内容
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=["PUT"])
def update_task(task_id):
    task = [t for t in tasks if t['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    # if 'title' in request.json and not isinstance(
    #         type(request.json['title']), unicode):
    #     abort(400)
    # if 'description' in request.json and not isinstance(
    #         type(request.json['description']), unicode):
    #     abort(400)
    #py3 不需要验证是否为unicode
    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description',
                                              task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])
    return jsonify({'task': task[0]})


# 删除一个task
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=["DELETE"])
def delete_task(task_id):
    task = [t for t in tasks if t['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


if __name__ == "__main__":
    app.run(debug=True)
