from flask import current_app as app
from flask import render_template, request, json, Response
from app.forms import SignUp, LoginForm, RecipeCreate


@app.route("/")
@app.route("/index")
def index():
    return render_template("home.html")


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    form = SignUp()
    return render_template("sign_up.html", title="Sign up", form=form) 



@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", title="Login", form=form) 


@app.route("/create_recipe", methods=["GET", "POST"])
def create_recipe():
    form = RecipeCreate()
    return render_template("create_recipe.html", title="Create new recipe", form=form)


