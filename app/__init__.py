from flask import Flask
from app import routes

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return "<h1>Hello World!<h1>"