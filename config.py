import os
from datetime import timedelta


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', '123su')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', '848jrmd')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)

    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'Suha2005Munthasir')
    MYSQL_DB = os.environ.get('MYSQL_DB', 'company_app')
