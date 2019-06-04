from flask import Flask,current_app
from settings.dev import DevConfig

app = Flask(__name__,template_folder="templates",static_folder='static')
app.config.from_object(DevConfig)

# 注册蓝图
from apps.users import users
from apps.roles import roles
app.register_blueprint(users,url_prefix='/users')
app.register_blueprint(roles,url_prefix='/roles')

@app.route("/")
def index():
    print( current_app.url_map )
    return "ok"

if __name__ == '__main__':
    app.run()
