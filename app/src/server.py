from flask import Flask
import mysql.connector

server = Flask(__name__)

mydb = mysql.connector.connect(
    host="172.29.0.3",
    user="root",
    password="password"
)

print(mydb)


@server.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    server.run(debug=True, host='0.0.0.0', port=5000)
