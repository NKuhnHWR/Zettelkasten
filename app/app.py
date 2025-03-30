from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///zettelkasten.db"
bootstrap = Bootstrap5(app)

db.init_app(app)

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)

class RegisterForm(FlaskForm):
    username = StringField("Name", validators=[DataRequired(), Length(4,10)])
    password = PasswordField("Passwort", validators=[DataRequired(), Length(8,30)])
    passwordrepeated = PasswordField("Passwort wiederholen", validators=[DataRequired(), Length(8,30)])
    submit = SubmitField()

with app.app_context():
    db.create_all()

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
        new_user = User(username = form.username.data, password = form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("dashboard"))
    return render_template("register.html", form=form)

@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")



