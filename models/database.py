# models/database.py

from flaskext.mysql import MySQL
from . import app

mysql = MySQL(app)

# MySQL configurations
app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_DB'] = 'PONTUAL'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)