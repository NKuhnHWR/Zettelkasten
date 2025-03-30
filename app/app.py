from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"
bootstrap = Bootstrap5(app)

class RegisterForm(FlaskForm):
    username = StringField("Name", validators=[DataRequired(), Length(4,10)])
    password = PasswordField("Passwort", validators=[DataRequired(), Length(8,30)])
    passwordrepeated = PasswordField("Passwort wiederholen", validators=[DataRequired(), Length(8,30)])
    submit = SubmitField()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    return render_template("register.html", form=form)

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")



