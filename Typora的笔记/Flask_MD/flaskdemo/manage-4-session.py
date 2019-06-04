from flask import Flask, session
from flask_session import Session

from settings.dev import DevConfig
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand


app = Flask(__name__,template_folder="templates",static_folder='static')
app.config.from_object(DevConfig)

# 启用flask-session
Session(app)

manager = Manager(app)

# 初始化SQLAlchemy
db = SQLAlchemy(app)

# 第一个参数是Flask的实例，
# 第二个参数是Sqlalchemy数据库实例
migrate = Migrate(app,db)
# manager是Flask-Script的实例，这条语句在flask-Script中添加一个db命令
# 参数1就是命令行调用数据迁移的命令前缀
manager.add_command('db',MigrateCommand)

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


@app.route("/set")
def index():
    session["username"] = "xiaoming"
    return "ok"

@app.route("/get")
def get_session():
    print(session.get("username"))
    return "ok"

if __name__ == '__main__':
    manager.run()
