from . import users

@users.route('/')
def user_home():
    return '个人中心'
