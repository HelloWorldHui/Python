import redis


class DevConfig(object):
    DEBUG = True
    SECRET_KEY = "luffycity" # session秘钥
    # 数据库配置
    # '数据库类型://账号:密码@数据库IP:端口/数据库名'
    SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1:3306/flaskdemo'
    # 动态追踪修改设置，如未设置只会提示警告
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    #查询时会显示原始SQL语句
    SQLALCHEMY_ECHO = True

    # session存储数据到redis的配置
    SESSION_TYPE = 'redis'  # session类型为redis
    SESSION_PERMANENT = False  # 如果设置为True，则关闭浏览器session就失效。
    SESSION_USE_SIGNER = False  # 是否对发送到浏览器上session的cookie值进行加密
    SESSION_KEY_PREFIX = 'session:'  # 保存到session中的值的前缀
    SESSION_REDIS = redis.Redis(host='127.0.0.1', port='6379')  # 用于连接redis的配置