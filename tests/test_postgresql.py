import pytest
from flask import Flask

from flask_postgresql import PostgreSQL
from tests.configuration import TestingConfig


class TestPostgreSQL:
    @pytest.fixture()
    def setup_teardown(self):
        print("\nsetup")
        yield
        print("\nteardown")

    def test_connection(self, setup_teardown):
        app = Flask(__name__)
        app.config.from_object(TestingConfig())

        db = PostgreSQL(app)

        with app.app_context():
            assert db.connection is not None
