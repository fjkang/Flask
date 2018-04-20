from flask_restful import Resource, reqparse, abort, request, fields, marshal, marshal_with
from werkzeug.security import generate_password_hash, check_password_hash

from api import api, db
from api.models import User

user_fields = {
    'uri': fields.Url('user'),
    'name': fields.String,
    'password': fields.String
}

class UserListApi(Resource):
    '''对用户列表操作'''

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'name', type=str, required=True, help='请输入name', location='json')
        self.reqparse.add_argument('password', type=str, location='json')
        super(UserListApi, self).__init__()

    @marshal_with(user_fields, envelope='users')
    def get(self):
        # 获取所有用户信息
        user_list = []
        users = User.query.all()
        for user in users:
            user_info = {
                'id': user.id,
                'name': user.username,
                'password': user.password_hash
            }
            user_list.append(user_info)
        return user_list

    def post(self):
        # 新建一个用户
        args = self.reqparse.parse_args()
        name = args['name']
        user = User(
            username=args['name'],
            password_hash=generate_password_hash(args['password']))
        db.session.add(user)
        db.session.commit()
        return {'msg': f'创建{name}成功'}, 201


class UserApi(Resource):
    '''通过id对用户操作'''

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, location='json')
        self.reqparse.add_argument('password', type=str, location='json')
        super(UserApi, self).__init__()

    @marshal_with(user_fields, envelope='user')
    def get(self, id):
        # 通过id获取用户信息
        user = User.query.filter_by(id=id).first()
        if user is None:
            abort(404)
        user_info = {
            'id': user.id,
            'name': user.username,
            'password': user.password_hash
        }
        return user_info

    def put(self, id):
        # 通过id修改用户信息
        user = User.query.filter_by(id=id).first()
        name = user.username
        if user is None:
            abort(404)
        args = self.reqparse.parse_args()
        if args['name']:
            user.username = args['name']
        user.password_hash = generate_password_hash(args['password'])
        db.session.add(user)
        db.session.commit()
        return {'msg': f'修改{name}成功'}

    def delete(self, id):
        # 通过id删除用户
        user = User.query.filter_by(id=id).first()
        name = user.username
        if user is None:
            abort(404)
        db.session.delete(user)
        db.session.commit()
        return {'msg': f'删除{name}成功'}

class UserPasswordApi(Resource):
    '''验证密码'''

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('password', type=str, location='json')
        super(UserPasswordApi, self).__init__()

    def post(self, id):
        # 验证密码
        user = User.query.filter_by(id=id).first()
        if user is None:
            abort(404)
        args = self.reqparse.parse_args()
        password = args['password']
        msg = check_password_hash(user.password_hash, password)
        return {'msg': f'密码:{msg}'}




api.add_resource(UserListApi, '/users', endpoint='users')
api.add_resource(UserApi, '/users/<int:id>', endpoint='user')
api.add_resource(UserPasswordApi, '/users/password/<int:id>', endpoint='password')

