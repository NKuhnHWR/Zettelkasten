# Importing all packages that aer needed
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from wtforms.validators import DataRequired, Length
from flask_sqlalchemy import SQLAlchemy
from bcrypt import hashpw, checkpw, gensalt

# Definition of the functions used for hashing and checking the password
def get_hashed_pw(plain_password):
    return hashpw(plain_password.encode("utf-8"), gensalt())

def check_password(plain_password, hashed_password):
    return checkpw(plain_password.encode("utf-8"), hashed_password=hashed_password)

#Setup app and database object
db = SQLAlchemy()
app = Flask(__name__)
app.config["SECRET_KEY"] = "secretkey"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///zettelkasten.db"
bootstrap = Bootstrap5(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
db.init_app(app)

#Definition for getting the current users ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#Definition of database model
class User(db.Model, UserMixin):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)

class Note(db.Model):
    __tablename__="notes"
    id = db.Column(db.Integer, unique = True, primary_key = True)
    ownerID = db.Column(db.String, nullable = False)
    content = db.Column(db.String, nullable = False)
    source = db.Column(db.String)
    category = db.Column(db.String, nullable = True)

class Category(db.Model):
    __tablename__="categories"
    id = db.Column(db.Integer, unique = True, primary_key = True)
    ownerID = db.Column(db.String, nullable = False)
    category_name = db.Column(db.String, nullable = False)

#Definition of forms including their fields
class RegisterForm(FlaskForm):
    username = StringField("Name", validators=[DataRequired(), Length(4,10)])
    password = PasswordField("Passwort", validators=[DataRequired(), Length(8,30)])
    passwordrepeated = PasswordField("Passwort wiederholen", validators=[DataRequired(), Length(8,30)])
    submit = SubmitField(label="Registrierung abschließen")

class LoginForm(FlaskForm):
    username = StringField("Name", validators=[DataRequired(), Length(4,10)])
    password = PasswordField("Passwort", validators=[DataRequired(), Length(8,30)])
    remember = BooleanField("Logindaten merken?")
    submit = SubmitField(label="Login bestätigen")

class NoteForm(FlaskForm):
    content = StringField("Notiz", validators=[DataRequired()])
    source = StringField("Herkunft der Notiz (Quelle)")
    category = SelectField("Kategorie der Notiz", coerce=int)
    submit = SubmitField(label="Notiz speichern")

class CategoryForm(FlaskForm):
    category_name = StringField("Name der Kategorie")
    submit = SubmitField(label="Kategorie anlegen")

#Creation of all database tables
with app.app_context():
    db.create_all()

#Definition of landingpage route
@app.route('/')
def index():
    if current_user.is_active:
        return render_template("index.html", user=current_user.username)
    return render_template("index.html")

#Definition of Login route
@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if current_user.is_active:
        return render_template("login.html", user=current_user.username)
    else:
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and check_password(form.password.data, user.password):
                login_user(user, remember=form.remember.data)
                flash("Der Login war erfolgreich!")
                return redirect(url_for("dashboard"))
            return render_template("login.html", form=form, error="Ungültige Logindaten!")
    return render_template("login.html", form=form)

#Definition of Register route
@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if current_user.is_active:
        return render_template("register.html", user=current_user.username)
    else:
        if form.validate_on_submit():
            if form.password.data == form.passwordrepeated.data:
                hashed_password = get_hashed_pw(form.password.data)
                new_user = User(username = form.username.data, password = hashed_password)
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for("dashboard"))
            else:
                return render_template("register.html", form=form, error="Die Passwörter sind nicht identisch!")  
    return render_template("register.html", form=form)

#Definition of Dashboard route
@app.route('/dashboard', methods=["GET", "POST"])
#in the next line is stated, that you have to be logged in to access this page
@login_required
def dashboard():
    form = CategoryForm()
    my_categories= []
    my_categories = db.session.query(
        Category.category_name,
        Category.id
    ).filter(Category.ownerID == current_user.id)
    #In this definition the tables have to be joined because the Note table only holds an ID and not the actual name that has to be shown
    my_notes = []
    my_notes = db.session.query(
        Note.content,
        Note.source,
        Note.id,
        Category.category_name
    ).join(Category, Note.category == Category.id) \
    .filter(Note.ownerID == current_user.id)
    if form.validate_on_submit():
        new_category = Category(ownerID = current_user.id, category_name = form.category_name.data)
        db.session.add(new_category)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template("dashboard.html", user=current_user.username, my_notes = my_notes, my_categories= my_categories, form = form)

#Definition for route to create a new note
@app.route('/note', methods=["GET", "POST"])
@login_required
def note():
    #avalilable_categories creates a filter on just the categories from this specific user
    available_categories = db.session.query(Category).filter(Category.ownerID == current_user.id)
    #categories_list creates a dictionary of the ids and category_names of available_category
    categories_list = [(i.id, i.category_name) for i in available_categories]
    form = NoteForm()
    #The next line passes the categories_list to the dropdown menu of the form
    form.category.choices = categories_list
    if form.validate_on_submit():
        new_note = Note(ownerID = current_user.id, content = form.content.data, source= form.source.data, category = form.category.data)
        db.session.add(new_note)
        db.session.commit()
        return redirect(url_for('dashboard'))
    return render_template("note.html", form=form)

#This route does'nt work perfectly because I didn't manage to implement the categories field
#This route should render the NoteForm with prefilled fields tht can be changed
@app.route('/change_note/<int:id>', methods=["GET", "POST"])
@login_required
def change_note(id):
    available_categories = db.session.query(Category).filter(Category.ownerID == current_user.id)
    categories_list = [(i.id, i.category_name) for i in available_categories]
    current_note = db.session.get(Note, id)
    current_note.category = db.session.query(
        Category.category_name
    ).join(Category, Note.category == Category.id) \
    .filter(Note.id == id)
    form = NoteForm(obj=current_note)
    if request.method == 'GET':
        if current_note:
            return(render_template("note.html", form = form))
    else:
        if request.method == 'POST':
            if form.validate():
                form.populate_obj(current_note)
                current_note.populate_lists([form.id.data])
                db.session.add(current_note)
                db.session.commit()
                flash('Notiz wurde aktualisiert.', 'success')
            else:
                flash('Validation error.', 'warning')
            return redirect(url_for('dashboard'))
    form.category.choices = categories_list
    if form.validate_on_submit():
        new_note = Note(ownerID = current_user.id, content = form.content.data, source= form.source.data, category = form.category.data)
        db.session.add(new_note)
        db.session.commit()
        return redirect(url_for("dashboard"))
    return render_template("note.html", form=form)

#This route shows the dashboard, filtered for one specific category
@app.route('/filtered_dashboard/<int:id>', methods=["GET", "POST"])
@login_required
def filtered_dashboard(id):
    my_categories= []
    my_categories = db.session.query(
        Category.category_name, 
        Category.id
    ).filter(Category.ownerID == current_user.id)
    my_notes = []
    my_notes = db.session.query(
        Note.content,
        Note.source,
        Note.id,
        Category.category_name
    ).join(Category, Note.category == Category.id) \
    .filter(Note.ownerID == current_user.id) \
    .filter(Note.category == id)
    return render_template("filtered_dashboard.html", user=current_user.username, my_notes = my_notes, my_categories= my_categories, category = Category.category_name)

#This route deletes a note and reloads the dashboard
@app.route('/delete_note/<int:id>', methods=["GET", "POST"]) 
@login_required
def delete_note(id):
    object = db.session.get(Note, id)
    db.session.delete(object)
    db.session.commit()
    return redirect(url_for("dashboard"))

#This route logs the user out and redirects to the index page
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

