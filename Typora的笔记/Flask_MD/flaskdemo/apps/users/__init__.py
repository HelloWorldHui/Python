from flask import Blueprint
# 等同于原来在 manage.py里面的 app = Flask()
users=Blueprint('users',__name__)

from .views import *