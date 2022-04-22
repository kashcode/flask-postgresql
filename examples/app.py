from flask import Flask
from flask_postgresql import PostgreSQL

app = Flask(__name__)
app.config["PG_HOST"] = "192.168.99.103"
app.config["PG_USERNAME"] = "test"
app.config["PG_PASSWORD"] = "test"
app.config["PG_DB"] = "test"
app.config["PG_PORT"] = "5432"

db = PostgreSQL(app)


@app.route("/")
def users():
    connection = db.connection

    with connection:
        with connection.cursor() as curs:
            curs.execute("""select usename from pg_catalog.pg_user""")
            data = curs.fetchone()

    return data[0]


if __name__ == "__main__":
    app.run(debug=True)
