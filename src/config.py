class Config():
    SECRET_KEY = 'FJedj@jwd!'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'root'
    MYSQL_DB = 'madretierra/users'

config = {
    'development': DevelopmentConfig
}