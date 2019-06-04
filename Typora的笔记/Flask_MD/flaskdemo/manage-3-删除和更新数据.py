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

@app.route("/delete")
def delete():
    """删除数据"""
    user = User.query.get(1)
    db.session.delete(user)
    db.session.commit()

    return "ok"


@app.route("/update")
def update():
    """更新数据"""
    user = User.query.get(2)
    user.born = "2000-10-01"
    user.name = "xiaowang"
    db.session.commit()
    return "ok"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
