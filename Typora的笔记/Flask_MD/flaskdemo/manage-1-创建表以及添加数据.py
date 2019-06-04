from flask import Flask
from settings.dev import DevConfig
from flask_sqlalchemy import SQLAlchemy

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

@app.route("/")
def index():
    return "ok"

@app.route("/add")
def add():
    # 数据库的基本操作
    """添加数据 add()"""
    role = Role(name="实习生")
    db.session.add(role)
    db.session.commit()

    role = Role(name="正式员工")
    db.session.add(role)
    db.session.commit()

    role = Role(name="优秀员工")
    db.session.add(role)
    db.session.commit()

    user = User(name="xiaoming", born="2018-10-01", email="qq.qq.com", password="123456",role_id=1)
    db.session.add(user)
    db.session.commit()

    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=1)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=3)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=1)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=3)
    us5 = User(name='tang', email='tang@163.com', password='158104', role_id=2)
    us6 = User(name='wu', email='wu@gmail.com', password='5623514', role_id=1)
    us7 = User(name='qian', email='qian@gmail.com', password='1543567', role_id=1)
    us8 = User(name='liu', email='liu@163.com', password='867322', role_id=2)
    us9 = User(name='li', email='li@163.com', password='4526342', role_id=3)
    us10 = User(name='sun', email='sun@163.com', password='235523', role_id=2)

    db.session.add_all([us1,us2,us3,us4,us5,us6,us7,us8,us9,us10])
    db.session.commit()

    return "ok"

if __name__ == '__main__':
    # 创建表,成功以后记得注释掉
    # db.create_all()

    app.run(host="0.0.0.0", port=80)
