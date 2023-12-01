from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt

app = Flask(__name__, static_url_path='', static_folder='views/static', template_folder='views')   
mysql = MySQL(app)

# MySQL configurations
#app.config['SECRET_KEY'] = 'mudar123' 
app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_DB'] = 'PONTUAL'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

# Mockup user database (replace this with a real user database)
users = {1: User(1), 2: User(2)}

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return users.get(int(user_id))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = int(request.form['user_id'])
        user = users.get(user_id)
        if user:
            login_user(user)
            return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
