from flask import Flask, request, redirect, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'Database'
app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'persondb'

mysql = MySQL(app)

@app.route('/persons', methods=['GET'])
def get_persons():
    _cursor = mysql.connection.cursor()
    sql_query = "SELECT * FROM persons"
    _cursor.execute(sql_query)
    rv = _cursor.fetchall()
    payload = []
    content = {}
    for result in rv:
        content = {'PersonID': result[0], 'Firstname': result[1], 'Lastname': result[2]}
        payload.append(content)
        content = {}
    return jsonify(payload)

@app.route('/person', methods=['POST'])
def add_person():
    _cursor = mysql.connection.cursor()
    sql_query = "INSERT INTO persons (Firstname, Lastname) VALUES (%s, %s)"
    val = (request.form['firstname'], request.form['lastname'])
    _cursor.execute(sql_query,val)
    mysql.connection.commit()
    return redirect('/persons')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)