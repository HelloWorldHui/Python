from flask import Flask
from settings.dev import DevConfig
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy import or_,and_,not_

app = Flask(__name__,template_folder="templates",static_folder='static')
app.config.from_object(DevConfig)

# 初始化SQLAlchemy
db = SQLAlchemy(app)

class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles' # 定义表名
    # 定义列对象
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 设置外键[用于1查询多的情况]
    us = db.relationship('User', backref='role',lazy='dynamic')
    # repr()方法类似于django的__str__，用于打印模型对象时显示的字符串信息
    def __repr__(self):
        return 'Role:%s'% self.name


# 创建数据模型必须继承db.Model
class User(db.Model):
    # 表选项
    __tablename__ = 'users' # 设置表名
    # 声明字段
    # db.Column(字段类型,选项)
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    born = db.Column(db.Date, index=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column( db.String(64) )
    # 设置外键
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    # __repr__方法类似于django的__str__，用于打印模型对象时显示的字符串信息
    def __repr__(self):
        return 'User:%s'% self.name

@app.route("/all")
def all():
    """all"""
    # 获取所有数据
    user_list = User.query.all()
    user_list_dict = []
    for user in user_list:
        user_list_dict.append({
            "id":user.id,
            "name": user.name
        })

    user_list_json = json.dumps(user_list_dict)
    return "ok"


@app.route("/filter_by")
def filter_by():
    # first获取一条数据
    user = User.query.filter_by(name="xiaoming").first()
    print(user)
    return "ok"

@app.route("/get")
def get():
    """get 根据主键查询对应数据"""
    user = User.query.get(10)
    print(user)
    return "ok"

@app.route("/mycount")
def mycount():
    mycount = User.query.count()
    print(mycount)
    return "ok"

@app.route("/like")
def like():
    # 查询name以字母"l"开头的
    # 模型类名.query.filter(模型类名.字段.startswith("字符串")).all()
    # endswith()  结尾

    user_list = User.query.filter(User.name.startswith("l")).all()
    print(user_list)
    return "ok"

@app.route("/logic1")
def logic1():
    # 取反
    user_list = User.query.filter(User.name!="xiaoming").all()
    print(user_list)
    return "ok"

@app.route("/logic2")
def logic2():
    # 或者,多条件
    user_list = User.query.filter( or_(User.name=="xiaoming",User.name=="li") ).all()
    print(user_list)
    return "ok"

@app.route("/logic3")
def logic3():
    # 并且,多条件
    user_list = User.query.filter( and_(User.role_id==1,User.id>5) ).all()
    print(user_list)
    return "ok"


if __name__ == '__main__':

    app.run(host="0.0.0.0", port=80)
