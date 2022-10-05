from flask import Flask, render_template, request
import json, time
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure db
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'dental'

mysql = MySQL(app)


@app.route('/', methods=['GET'])
def home_page():
    data_set = {'Page': "Homepage", "Message": "Succesfully loaded to the home page", 'Timestamp': time.time()}

    json_value = json.dumps(data_set)

    return json_value

@app.route('/create-user', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        
        userDetails = request.form

        # Form Date
        name = userDetails['name']
        email = userDetails['email']

        # Insertion to DB
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user(name, email) VALUES(%s, %s)", (name, email))
        
        mysql.connection.commit()

        cur.close()

        return f'Success the {name} and {email} is now inserted to the database'

    return render_template('index.html')

@app.route('/users')
def users():

    # Selection from DB
    cur = mysql.connection.cursor()
    res = cur.execute("SELECT * FROM user")

    if res > 0:
        userDetails = cur.fetchall()

        return render_template('users.html', userDetails=userDetails)

# TO DO -> Fetch the userId of the User
# @app.route('/fetch_user')
# def fetch():

#     cur = mysql.connection.cursor()
#     res = cur.execute("SELECT * FROM user where ")


if __name__ == '__main__':
    app.run(debug=True)
