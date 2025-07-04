from flask import Flask, render_template, request, redirect, flash, session, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email


app = Flask(__name__)
 # needed for flash()
app.secret_key = "supersecretkey" 

# Config SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo1.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Todo model
class Todo(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.Sno} - {self.title}"

# Define a User model for profile
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    bio = db.Column(db.String(300), nullable=True)

#home
@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']

        if title.strip() and desc.strip():
            todo1 = Todo(title=title, desc=desc)
            db.session.add(todo1)
            db.session.commit()

    all_todos = Todo.query.all()
    return render_template("index.html", all_todos=all_todos)

#Delete
@app.route('/delete/<int:Sno>')
def delete(Sno):
    todo_to_delete = Todo.query.filter_by(Sno=Sno).first()
    if todo_to_delete:
        db.session.delete(todo_to_delete)
        db.session.commit()
    return redirect("/")

#Update
@app.route('/update/<int:Sno>', methods=['GET', 'POST'])
def update(Sno):
    todo = Todo.query.filter_by(Sno=Sno).first()

    if request.method == 'POST':
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        db.session.commit()
        return redirect("/")

    return render_template("update.html", todo=todo)

    
#about
@app.route('/about')
def about():
    return render_template("About.html")

#register
@app.route('/register')
def register():
    return render_template("register.html")

#feedback
@app.route('/feedback')
def feedback():
    return render_template("feedback.html")

#profile
@app.route('/profile', methods=['GET'])
def profile():
    
    user = User.query.first()
    if not user:
        user = User(name="Vinayak Sharma", email="Vinayak@gmail.com", bio="Love building things with Python & Flask.")
        db.session.add(user)
        db.session.commit()
    return render_template("profile.html", user=user)

#profile Update
@app.route('/profile/update', methods=['POST'])
def update_profile():
    user = User.query.first()
    if not user:
        user = User(name="Vinayak Sharma", email="Vinayak@gmail.com", bio="Love building things with Python & Flask.")
        db.session.add(user)

    user.name = request.form['name']
    user.email = request.form['email']
    user.bio = request.form['bio']
    db.session.commit()
    flash("Profile updated successfully!", "success")
    return redirect(url_for('profile'))

#login form
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Log In')

@app.route('/login', methods=['GET', 'POST'])
@app.route('/Login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        
        flash('Login successful!', 'success')
        return redirect(url_for('hello_world')) 
    return render_template('login.html', form=form)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=5000)










