from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "1"

@app.route("/hello")
def index():
	flash("what's your name? ... WHAT IS YOUR NAME??")
	return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
	flash("FUCK YOU " + str(request.form['name_input']))
	request.form['name_input']
	return render_template("index.html")