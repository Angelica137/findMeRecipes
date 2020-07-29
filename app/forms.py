from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Optional


class LoginForm(FlaskForm):
    email = StringField("Email", [DataRequired()])
    password = StringField("Password", [DataRequired()])
    submit = SubmitField("Login")


class SignUp(FlaskForm):
    email = StringField("Email", [DataRequired()])
    password = StringField("Password", [DataRequired()])
    confirm_password = StringField("Confirm password", [DataRequired()])
    submit = SubmitField("Sign up")


class RecipeCreate(FlaskForm):
    recipe_name = StringField("Recipe name", [DataRequired()])
    recipe_description = TextAreaField("Description", [Optional()])
    servings = IntegerField("Servings", [DataRequired()])
    submit = SubmitField("Save")