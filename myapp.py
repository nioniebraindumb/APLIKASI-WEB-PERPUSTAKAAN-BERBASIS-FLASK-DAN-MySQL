""" # import library third party
from flask import Flask, render_template
from flask_mysqldb import MySQL

# init main app
app = Flask(__name__)

# database configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskmysql'

#init mysql
mysql = MySQL(app)

# set route dafault
@app.route('/')

# function home
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    return render_template('home.html', users=data)

if __name__ == '__main__':
    app.run(debug=True)
    
 """