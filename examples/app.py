import logging

from flask import Flask
from flask_postgresql import PostgreSQL

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-8s %(name)s %(threadName)s : %(message)s'
)

app = Flask(__name__)
app.config["PG_HOST"] = "192.168.99.103"
app.config["PG_USERNAME"] = "test"
app.config["PG_PASSWORD"] = "test"
app.config["PG_DB"] = "test"
app.config["PG_PORT"] = "5432"

postgres = PostgreSQL(app)


@app.route("/")
def users():
    connection = postgres.connection

    with connection:
        with connection.cursor() as curs:
            curs.execute("""select usename from pg_catalog.pg_user""")
            data = curs.fetchone()

    return data[0]


if __name__ == "__main__":
    app.run(debug=True)
