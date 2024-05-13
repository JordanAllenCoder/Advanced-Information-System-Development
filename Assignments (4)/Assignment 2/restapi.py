import flask
from flask import jsonify
from flask import request
from sql import create_connection
from sql import execute_read_query
import creds

#setting up an application name
app = flask.Flask(__name__) #sets up the application
app.config["DEBUG"] = True #allow to show errors in browser

#default url without any routing as GET request
@app.route('/', methods=['GET'])
def home():
    return "<h1> Manage the Gems! </h1>"

#endpoint to get a single gem
@app.route('/api/gem', methods=['GET'])
def api_users_id():
    if 'id' in request.args: 
        id = int(request.args['id'])
    else:
        return 'ERROR: No ID provided!'
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "SELECT * FROM gem"
    gem = execute_read_query(conn, sql)
    results = []

    for gem in gem:
        if gem['id'] == id:
            results.append(gem)
    return jsonify(results)

#add gem as POST
@app.route('/api/gem', methods=['POST'])
def add_example():
    request_data = request.get_json()
    id = request_data['id']
    gemtype = request_data['gemtype']
    gemcolor = request_data['gemcolor']
    carat = request_data['carat']
    price = request_data['price']
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    cursor = conn.cursor(dictionary=True)
    sqll = f"INSERT INTO gem (id, gemtype, gemcolor, carat, price) VALUES ('{id}', '{gemtype}', '{gemcolor}', '{carat}', '{price}')"
    cursor.execute(sqll)
    conn.commit()
    return 'Add request was successful'

@app.route('/api/gem', methods=['DELETE'])
def delete_example():
    if 'id' in request.args: 
        id = int(request.args['id'])
    else:
        return 'ERROR: No ID provided!'
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    cursor = conn.cursor(dictionary=True)
    sqlll = f'DELETE FROM gem WHERE id = {id}'
    cursor.execute(sqlll)
    conn.commit()
    return 'Delete request was successful'

#add gem as PUT
@app.route('/api/gem', methods=['PUT'])
def update_example():
    request_data = request.get_json()
    id = request_data['id']
    gemtype = request_data['gemtype']
    gemcolor = request_data['gemcolor']
    carat = request_data['carat']
    price = request_data['price']
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    cursor = conn.cursor(dictionary=True)
    sqllll=f"UPDATE gem SET gemtype = '{gemtype}', gemcolor = '{gemcolor}', carat = '{carat}', price = '{price}' WHERE id = '{id}'"
    cursor.execute(sqllll)
    conn.commit()
    return 'Update request was successful'

app.run()