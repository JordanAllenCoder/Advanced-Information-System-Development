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
    return "<h1> Flight Planner </h1>"  # this is just to get going. I like to use this as a title page

# created information for the single user to login with
singleuser = [
    {
        # single user
        'username': 'username',
        'password': 'password',
        'role': 'primary user',
        'token': '12345',
        'userinfo': 'This user has full access to the UI'
    },
]

# simple login API to authenticate the user
@app.route('/api/login', methods=['GET'])
def api_login():
    username = request.headers['username'] 
    password = request.headers['password']
    for au in singleuser: #loop over all users and find one that is authorized to access
        if au['username'] == username and au['password'] == password: #found an authorized user
            sessiontoken = au['token']
            userInfo = au['userinfo']
            returnInfo = []
            returnInfo.append(au['role'])
            returnInfo.append(sessiontoken)
            returnInfo.append(userInfo)
        
            return jsonify(returnInfo)  # returns the users role, token, and info
    return 'SECURITY ERROR' # Error reciept


#endpoint to get all airports using GET
@app.route('/api/airports', methods=['GET'])  # set endpoint information for API
def api_airports():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    sql = "SELECT * FROM airports"  # sql command
    airports = execute_read_query(conn, sql)
    results = []  # make a list 
    results.append(airports)  # add airports to the list
    return jsonify(results)
    # This endpoint will allow for the user to GET information from the sql database 

# endpoint to add airport as POST
@app.route('/api/airports', methods=['POST'])  # set endpoint information for API
def add_airports():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    cursor = conn.cursor(dictionary=True)
    request_data = request.get_json()  # set request for json in API. request new airports data
    airportcode = request_data['airportcode']
    airportname = request_data['airportname']
    country = request_data['country']
    sqll = f"INSERT INTO airports (airportcode, airportname, country) VALUES ('{airportcode}', '{airportname}', '{country}')"
    cursor.execute(sqll) # execute the sql code from above and commit the changes using the next line 
    conn.commit()
    return 'Add request was successful'  # reciept
    # This endpoint will allow the user to POST a new record into the airports table of the sql database.

#update the airports with PUT
@app.route('/api/airports', methods=['PUT'])  # set endpoint information for API
def update_airport():
    if 'id' in request.args: 
        id = int(request.args['id'])  # get specific id for the desired airport to update
    else:
        return 'ERROR: No ID provided!'  # error code 
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    cursor = conn.cursor(dictionary=True)
    request_data = request.get_json()
    airportcode = request_data['airportcode']
    airportname = request_data['airportname']
    country = request_data['country']
    sqllll=f"UPDATE airports SET airportcode = '{airportcode}', airportname = '{airportname}', country = '{country}' WHERE id = {id}"  
    cursor.execute(sqllll)  
    conn.commit()
    return 'Update request was successful'  #receipt

# endpoint to delete an airport using DELETE
@app.route('/api/airports', methods=['DELETE'])  # set enpoint information for API
def delete_airports():
    if 'airportname' in request.args: 
        airportname = request.args['airportname']  # get specific id for desired airport to delete
    else:
        return 'ERROR: No name provided!'  # error message
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    cursor = conn.cursor(dictionary=True)
    sqlll = f"DELETE FROM airports WHERE airportname = '{airportname}'"  # sql code to delete a airport using the id
    cursor.execute(sqlll)
    conn.commit()
    return 'Delete request was successful'  # receipt

#endpoint to get all planes using GET
@app.route('/api/planes', methods=['GET'])  # set endpoint information for API
def api_planes():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    planes_sql = "SELECT * FROM planes"  # sql command
    planes = execute_read_query(conn, planes_sql)
    results = []  # make a list 
    results.append(planes)  # add planes to the list
    return jsonify(results)
    # This endpoint will allow for the user to GET information from the sql database 

# endpoint to add planes as POST
@app.route('/api/planes', methods=['POST'])  # set endpoint information for API
def add_planes():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    cursor = conn.cursor(dictionary=True)
    request_data = request.get_json()  # set request for json in API. request new planes data
    make = request_data['make']
    model = request_data['model']
    year = request_data['year']
    capacity = request_data['capacity']
    planes_sqll = f"INSERT INTO planes (make, model, year, capacity) VALUES ('{make}', '{model}', {year}, {capacity})"
    cursor.execute(planes_sqll) # execute the sql code from above and commit the changes using the next line 
    conn.commit()
    return 'Add request was successful'  # reciept
    # This endpoint will allow the user to POST a new record into the airports table of the sql database.

#update planes with PUT
@app.route('/api/planes', methods=['PUT'])  # set endpoint information for API
def update_planes():
    if 'id' in request.args: 
        id = int(request.args['id'])  # get specific id for the desired plane to update
    else:
        return 'ERROR: No ID provided!'  # error code 
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    cursor = conn.cursor(dictionary=True)
    request_data = request.get_json()
    make = request_data['make']
    model = request_data['model']
    year = request_data['year']
    capacity = request_data['capacity']
    planes_sqllll=f"UPDATE planes SET make = '{make}', model = '{model}', year = {year}, capacity = {capacity} WHERE id = {id}"  
    cursor.execute(planes_sqllll)  
    conn.commit()
    return 'Update request was successful'  #receipt

# endpoint to delete a plane using DELETE
@app.route('/api/planes', methods=['DELETE'])  # set enpoint information for API
def delete_planes():
    if 'model' in request.args: 
        model = request.args['model']  # get specific id for desired plane to delete
    else:
        return 'ERROR: No model provided!'  # error message
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    cursor = conn.cursor(dictionary=True)
    planes_sqlll = f"DELETE FROM planes WHERE model = '{model}'"  # sql code to delete a plane using the id
    cursor.execute(planes_sqlll)
    conn.commit()
    return 'Delete request was successful'  # receipt

#jordan this is where you are at right now
#endpoint to get all flights
@app.route('/api/flights', methods=['GET'])  # set endpoint information for API
def api_flights():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    flights_sql = "SELECT * FROM flights"  # sql command
    flights = execute_read_query(conn, flights_sql)
    results = []  # make a list 
    results.append(flights)  # add flights to the list
    return jsonify(results)
    # This endpoint will allow for the user to GET information from the sql database 

# endpoint to add a flight as POST
@app.route('/api/flights', methods=['POST'])  # set endpoint information for API
def add_flights():
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    cursor = conn.cursor(dictionary=True)
    request_data = request.get_json()  # set request for json in API. request new flight data
    planeid = request_data['planeid']
    airportfromid = request_data['airportfromid']
    airporttoid = request_data['airporttoid']
    date = request_data['date']
    flights_sqll = f"INSERT INTO flights (planeid, airportfromid, airporttoid, date) VALUES ({planeid}, {airportfromid}, {airporttoid}, '{date}')"
    cursor.execute(flights_sqll) # execute the sql code from above and commit the changes using the next line '
    conn.commit()
    return 'Add request was successful'  # reciept
    # This endpoint will allow the user to POST a new record into the flights table of the sql database.

# endpoint to delete a flight using DELETE
@app.route('/api/flights', methods=['DELETE'])  # set enpoint information for API
def delete_flights():
    if 'date' in request.args: 
        date = request.args['date']  # get specific id for desired flight to delete
    else:
        return 'ERROR: No date provided!'  # error message
    myCreds = creds.Creds()
    conn = create_connection(myCreds.conString, myCreds.userName, myCreds.password, myCreds.dbName)
    cursor = conn.cursor(dictionary=True)
    flights_sqllll = f"DELETE FROM flights WHERE date = '{date}'"  # sql code to delete a flight using the id
    cursor.execute(flights_sqllll)
    conn.commit()
    return 'Delete request was successful'  # receipt
    # This endpoint will allow the user to DELETE a record from the flights table of the sql database.

app.run()
