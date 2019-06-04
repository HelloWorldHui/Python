from . import roles

@roles.route("/")
def home():
    return "role_list"