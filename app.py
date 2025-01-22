from flask import Flask, render_template, redirect, request,flash,url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Seun%40112@localhost/todoapp'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://emmyily:Seun%40112@localhost/tododb'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Seun%40112@127.0.0.1:3306/tododb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'whateverjustgetonwithit!'
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
migrate = Migrate(app, db)

#for user login
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(225), nullable=False)
    tasks = db.relationship('Task', backref='author', lazy=True)

    def set_password(self, password):
        self.password = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password)


    #to display data in database
    def __repr__(self):
        return '<User {}>'.format(self.username)


#for the tasks
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),unique=True)
    description = db.Column(db.String(100),unique=True)
    done = db.Column(db.Boolean, default='Not completed')
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, name = 'fk_user_id')

    def __repr__(self):
        return '<Task %r>' % self.id

with app.app_context():
    db.create_all()



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/', methods=['GET', 'POST'])
@login_required
def homepage():  # put application's code here
    if request.method == 'POST':
        title_form = request.form['title']
        description_form = request.form['description']
        done = 'done' in request.form#To set a default value for (done) since it has a view of it's own, it needs to accept a default value when adding a task
        new_task = Task(title=title_form,description=description_form,done=done,user_id=current_user.id)#create object of your class
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(f'ERROR{e}')

    v =Task.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', v=v, title='Homepage',user=current_user)


@app.route('/done/<int:id>', methods=['GET', 'POST'])
def completed(id:int):  # put application's code here
    status_checker = Task.query.get_or_404(id)
    status_checker.done = not status_checker.done
    try:
        db.session.commit()
        return redirect('/')
    except Exception as e:
        print(f'ERROR{e}')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id:int):  # put application's code here
    edit_task = Task.query.get_or_404(id)
    if request.method == 'POST':
        edit_task.title = request.form['title']#request for the forms
        edit_task.description = request.form['description']#request for the forms
        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(f'ERROR{e}')
    else:
        return render_template('edit.html', task=edit_task)




@app.route('/delete/<int:id>', methods=['GET','POST'])
def delete(id:int):  # put application's code here
    delete_task = Task.query.get_or_404(id)#make a variable that grabs the object's id
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        print(f'ERROR{e}')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            flash('Login successful!', 'success')
            login_user(user)
            return redirect(url_for('homepage'))
        else:
            flash('Invalid credentials, please try again.', 'danger')

    return render_template('login.html', title='login')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match. Please try again.', 'danger')
            return redirect(url_for('register'))

        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            flash('Username or email already exists. Please choose another one.', 'danger')
            return redirect(url_for('register'))

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        try:
            db.session.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('welcome'))
        except Exception as e:
            print(f'ERROR: {e}')
            db.session.rollback()
            flash('An error occurred during registration. Please try again.', 'danger')

    return render_template('register.html', title='register')


@app.route('/welcome', methods=['GET','POST'])
def welcome():
    return render_template('welcome.html', title='welcome')

@app.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    return render_template('welcome.html', title='welcome')

if __name__ == '__main__':
    app.run()
