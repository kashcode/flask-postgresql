import os


class TestingConfig:
    TESTING = True
    SECRET_KEY = 1234
    PG_HOST = os.getenv('PG_HOST')
    PG_USERNAME = os.getenv('PG_USERNAME')
    PG_PASSWORD = os.getenv('PG_PASSWORD')
    PG_PORT = os.getenv('PG_PORT')
    PG_DB = os.getenv('PG_DB')
