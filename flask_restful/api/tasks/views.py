from flask_restful import Resource, reqparse, abort, request, fields, marshal, marshal_with

from api import api, db
from api.models import Task

task_fields = {
    'title': fields.String,
    'description': fields.String,
    'done': fields.Boolean,
    'uri': fields.Url('task')
}


class TaskListApi(Resource):
    '''获取所有task的api'''

    def __init__(self):
        # 添加字段的格式要求
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'title', type=str, required=True, help='请输入title', location='json')
        self.reqparse.add_argument(
            'description', type=str, default="", location='json')
        super(TaskListApi, self).__init__()

    @marshal_with(task_fields, envelope='tasks')
    # marshl_with可以处理迭代对象
    def get(self):
        # 获取所有task
        task_list = []
        tasks = Task.query.all()
        for task in tasks:
            task_info = {
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'done': task.done
            }
            task_list.append(task_info)
        return task_list

    def post(self):
        # 创建一个task
        args = self.reqparse.parse_args()
        title = args['title']
        task = Task(
            title=args['title'], description=args['description'], done=False)
        db.session.add(task)
        db.session.commit()
        return {'msg': f'创建task:{title}成功'}, 201


class TaskApi(Resource):
    '''获取一个task的api'''

    def __init__(self):
        # 添加字段的格式要求
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(TaskApi, self).__init__()

    @marshal_with(task_fields, envelope='task')
    def get(self, id):
        # 通过id获取task
        task = Task.query.filter_by(id=id).first()
        if task == None:
            abort(404)
        task_info = {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'done': task.done
        }
        return task_info

    def put(self, id):
        # 通过id修改task
        task = Task.query.filter_by(id=id).first()
        if task == None:
            abort(404)
        title = task.title
        args = self.reqparse.parse_args()
        if args['title'] != None:
            task.title = args['title']
        if args['description'] != None:
            task.description = args['description']
        if args['done'] != None:
            task.done = args['done']
        db.session.add(task)
        db.session.commit()
        return {'msg': f'修改task:{title}成功'}

    def delete(self, id):
        # 通过id删除task
        task = Task.query.filter_by(id=id).first()
        if task == None:
            abort(404)
        title = task.title
        db.session.delete(task)
        db.session.commit()
        return {'msg': f'删除task:{title}成功'}


api.add_resource(TaskApi, '/todo/api/v1.0/tasks/<int:id>', endpoint='task')
api.add_resource(TaskListApi, '/todo/api/v1.0/tasks', endpoint='tasks')