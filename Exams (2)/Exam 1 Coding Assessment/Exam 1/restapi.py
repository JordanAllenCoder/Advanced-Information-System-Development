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
    return "<h1> Watch Collection Managment! </h1>"  # this is just to get going. I like to use this as a title page

#endpoint to get all watches sorted by profit
@app.route('/api/watch', methods=['GET'])  # set endpoint information for API
def api_all():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "SELECT * FROM watches"  # sql command
    watch = execute_read_query(conn, sql)
    results = []  # make a list 
    results.append(watch)  # add watches to the list
    results.sort(key = lambda i: i[2]) # failed attempt to sort the list. I ran out of time but I think I need to split my list in order to use this index method
    return jsonify(results)
    # This endpoint will allow for the user to GET information from the sql database 

# endpoint to add watch as POST
@app.route('/api/watch', methods=['POST'])  # set endpoint information for API
def add_watch():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    cursor = conn.cursor(dictionary=True)
    request_data = request.get_json()  # set request for json in API. request new watch data
    id = request_data['id']
    make = request_data['make']
    model = request_data['model']
    type = request_data['type']
    purchaseprice = request_data['purchaseprice']
    saleprice = request_data['saleprice']
    sqll = f"INSERT INTO watches (id, make, model, type, purchaseprice, saleprice) VALUES ('{id}', '{make}', '{model}', '{type}', '{purchaseprice}', '{saleprice}')"
    cursor.execute(sqll) # execute the sql code from above and commit the changes using the next line 
    conn.commit()
    return 'Add request was successful'  # reciept
    # This endpoint will allow the user to POST a new record into the watches table of the sql database.

#update the saleprice of a watch with PUT
@app.route('/api/watch', methods=['PUT'])  # set endpoint information for API
def update_watch():
    if 'id' in request.args: 
        id = int(request.args['id'])  # get specific id for the desired watch to update
    else:
        return 'ERROR: No ID provided!'  # error code 
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    cursor = conn.cursor(dictionary=True)
    request_data = request.get_json()
    saleprice = request_data['saleprice']  # request the new sale price using json in API
    sqllll=f"UPDATE watches SET saleprice = '{saleprice}' WHERE id = '{id}'"  # update the watches table of the database with the saleprice using the id
    cursor.execute(sqllll)  
    conn.commit()
    return 'Update request was successful'  #receipt

# endpoint to delete a watch using DELETE
@app.route('/api/watch', methods=['DELETE'])  # set enpoint information for API
def delete_watches():
    if 'id' in request.args: 
        id = int(request.args['id'])  # get specific id for desired watch to delte
    else:
        return 'ERROR: No ID provided!'  # error message
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    cursor = conn.cursor(dictionary=True)
    sqlll = f'DELETE FROM watches WHERE id = {id}'  # sql code to delete a watch using the id
    cursor.execute(sqlll)
    conn.commit()
    return 'Delete request was successful'  # receipt

app.run()
