from flask import Flask, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from wtforms.validators import DataRequired, Length
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///zettelkasten.db"
bootstrap = Bootstrap5(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

db.init_app(app)

class User(db.Model, UserMixin):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)

class RegisterForm(FlaskForm):
    username = StringField("Name", validators=[DataRequired(), Length(4,10)])
    password = PasswordField("Passwort", validators=[DataRequired(), Length(8,30)])
    passwordrepeated = PasswordField("Passwort wiederholen", validators=[DataRequired(), Length(8,30)])
    submit = SubmitField()

class LoginForm(FlaskForm):
    username = StringField("Name", validators=[DataRequired(), Length(4,10)])
    password = PasswordField("Passwort", validators=[DataRequired(), Length(8,30)])
    remember = BooleanField("Logindaten merken?")
    submit = SubmitField()

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    if current_user.is_active:
        return render_template("index.html", user=current_user.username)
    return render_template("index.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user, remember=form.remember.data)
            flash("Der Login war erfolgreich!")
            return redirect(url_for("dashboard"))
        return render_template("login.html", form=form, error="Ungültige Logindaten!")
    return render_template("login.html", form=form)

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data == form.passwordrepeated.data:
            new_user = User(username = form.username.data, password = form.password.data)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for("dashboard"))
        else:
          return render_template("register.html", form=form, error="Die Passwörter sind nicht identisch!")  
    return render_template("register.html", form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

