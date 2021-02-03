import os

import pytest
from flask import Flask

from flask_postgresql import PostgreSQL


class TestPostgreSQL:
    @pytest.fixture()
    def setup_teardown(self):
        print("\nsetup")
        yield
        print("\nteardown")

    def test_connection(self, setup_teardown):
        app = Flask(__name__)
        app.config['SECRET_KEY'] = '1234'
        app.config['PG_HOST'] = os.getenv('PG_HOST')
        app.config['PG_USERNAME'] = os.getenv('PG_USERNAME')
        app.config['PG_PASSWORD'] = os.getenv('PG_PASSWORD')
        app.config['PG_PORT'] = os.getenv('PG_PORT')
        app.config['PG_DB'] = os.getenv('PG_DB')

        db = PostgreSQL(app)

        with app.app_context():
            assert db.connection is not None
