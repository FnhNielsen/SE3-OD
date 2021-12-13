from flask import Flask, request, redirect, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'mysqldb'
app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = 'sql'
app.config['MYSQL_DB'] = 'persondb'

mysql = MySQL(app)

@app.route('/persons', methods=['GET'])
def get_persons():
    _cursor = mysql.connection.cursor()
    sql_query = "SELECT * FROM Person"
    _cursor.execute(sql_query)
    data_set = _cursor.fetchall()
    payload = []
    data = {}
    for res in data_set:
        data = {'PersonID': res[0], 'Firstname': res[1], 'Lastname': res[2]}
        payload.append(data)
        data = {}
    return jsonify(payload)

@app.route('/person', methods=['POST'])
def add_person():
    _cursor = mysql.connection.cursor()
    sql_query = "INSERT INTO Person (Firstname, Lastname) VALUES (%s, %s)"
    val = (request.form['Firstname'], request.form['Lastname'])
    _cursor.execute(sql_query,val)
    mysql.connection.commit()
    return redirect('/persons')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)