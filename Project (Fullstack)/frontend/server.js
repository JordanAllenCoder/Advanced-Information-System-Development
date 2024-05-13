// load the things we need
var express = require('express');
var app = express();
const bodyParser  = require('body-parser');

// required module to make calls to a REST API
const axios = require('axios');

app.use(bodyParser.urlencoded());

// set the view engine to ejs
app.set('view engine', 'ejs');


// API to get flights. These API's are the reason I have had so much trouble with this project. 
// I can get the data in my console but I do not know how to store the data. I have tried the methods used in the 
// homeworks and exam 2 but they have failed. I tried some of the methods used in the in-class 
// examples and those also failed. I know I am close but I have not been able to GET the flights. Updated 12/6/2022 I knew I was close.
app.get('/flights', function(req, res) {

    //local API call to my Python API that delivers flights
    axios.get(`http://127.0.0.1:5000/api/flights`)
    .then((response)=>{
        
        var flights = response.data[0];  // I DID IT !!! I thought I had tried every way possible to make the requested data indexable. I put [] EVERYWHERE and it would respond with (object, object) on the server. I moved the [] from [request.data] to request.data[0] and it solved the problem.
        var tagline = "Hello, These are your currently scheduled flights!";
        console.log(flights);
         // use res.render to load up an ejs view file
        res.render('pages/flights', {
            flights: flights,
            tagline: tagline
        });
    }); 
});


// this is where flights are deleted at. the parsed date is added as the search token and the API and backend execute the operation.
// NOTE: The server does not crash with the function error. The backend executes the delete in the mySQL database. 
// all that has to be done is to go back and refresh the page. The record will be deleted and the GET will be updated.
app.post('/process_form_del_flights', function(req, res){
    // create a variable to hold the date parsed from the request body
    var date = req.body.date1

   console.log("The date selected to delete was: " + date);
   axios.delete('http://127.0.0.1:5000/api/flights?date='+date)
   .then((response)=>{
       let flights = response.data;
       console.log(flights);
       res.render('pages/flights', {
           flights: flights
       });
    })
})


// this is where flights are added. I have not been able to get this operation to work. I have spent 
// the last two days trying to get the POST to work but I have exhausted all ideas and there are 
// absolutely zero resources online. If you could please fix one of my POST operations where I am 
// to create a record, I would GREATLY appreciate it. I just can’t figure out what I am doing wrong. 
// I am positive that if I knew how to create a record, I would be able to update one too.
app.post('/process_form_flights', function(req, res){

    var planeid = req.body.planeid
    var airportfromid = req.body.airportfromid
    var airporttoid = req.body.airporttoid
    var date = req.body.date

    console.log("Successfully completed");
    axios.post('http://127.0.0.1:5000/api/flights')
    .then((response)=>{
        let flights = {"planeid": planeid, "airportfromid": airportfromid, "airporttoid": airporttoid, "date": date};
        response.post(flights);
        console.log(flights);
        res.render('pages/flights', {
            flights: flights
       });
    })
})


// this is where flights are updated. I have not been able to get this operation to work. I have spent 
// the last two days trying to get the POST to work but I have exhausted all ideas and there are 
// absolutely zero resources online. If you could please fix one of my POST operations where I am 
// to create a record, I would GREATLY appreciate it. I just can’t figure out what I am doing wrong. 
// I am positive that if I knew how to create a record, I would be able to update one too.
app.post('/process_form_update_flights', function(req, res){

    var planeid = req.body.planeid2
    var airportfromid = req.body.airportfromid2
    var airporttoid = req.body.airporttoid2
    var date = req.body.date2

    console.log("Successfully completed");
    axios.post('http://127.0.0.1:5000/api/flights')
    .then((response)=>{
        let flights = {"planeid": planeid, "airportfromid": airportfromid, "airporttoid": airporttoid, "date": date};
        response.put(flights);
        console.log(flights);
        res.render('pages/flights', {
            flights: flights
       });
    })
})


// API to get airports. These API's are the reason I have had so much trouble with this project. 
// I can get the data but I do not know how to store the data. I have tried the methods used in the 
// homeworks and exam 2 but they have failed. I tried some of the methods used in the in-class 
// examples and those also failed. I know I am close but I have not been able to GET the airports.
app.get('/airports', function(req, res) {

    //local API call to my Python API that delivers airports
    axios.get(`http://127.0.0.1:5000/api/airports`)
    .then((response)=>{
        
        var airports = response.data[0];   
        results = airports
        var tagline = "Hello, These are your current airports!";
        console.log(airports);
         // use res.render to load up an ejs view file
        res.render('pages/airports', {
            airports: airports,
            tagline: tagline
        });
    }); 
});


// this is where airports are deleted at. the parsed airportname is added as the search token and the API and backend execute the operation.
// NOTE: The server does not crash with the function error. The backend executes the delete in the mySQL database. 
// all that has to be done is to go back and refresh the page. The record will be deleted and the GET will be updated.
app.post('/process_form_del_airports', function(req, res){
    // create a variable to hold the airportname parsed from the request body
    var airportname = req.body.airportname1

   console.log("Deleted: " + airportname);
   axios.delete('http://127.0.0.1:5000/api/airports?airportname='+airportname)
   .then((response)=>{
       let airports = response.data;
       console.log(airports);
       res.render('pages/airports', {
           airports: airports
       });
    })
})


// this is where airports are added. I have not been able to get this operation to work. I have spent 
// the last two days trying to get the POST to work but I have exhausted all ideas and there are 
// absolutely zero resources online. If you could please fix one of my POST operations where I am 
// to create a record, I would GREATLY appreciate it. I just can’t figure out what I am doing wrong. 
// I am positive that if I knew how to create a record, I would be able to update one too.
app.post('/process_form_airports', function(req, res){

    var airportcode = req.body.airportcode
    var airportname = req.body.airportname
    var country = req.body.country

   console.log("Successfully completed");
   axios.post('http://127.0.0.1:5000/api/airports')
   .then((response)=>{
        let airports = {"airportcode": airportcode, "airportname": airportname, "country": country};
        response.post(airports);
        console.log(airports);
        res.render('pages/airports', {
            airports: airports
       });
    })
})


// this is where airports are updated. I have not been able to get this operation to work. I have spent 
// the last two days trying to get the POST to work but I have exhausted all ideas and there are 
// absolutely zero resources online. If you could please fix one of my POST operations where I am 
// to create a record, I would GREATLY appreciate it. I just can’t figure out what I am doing wrong. 
// I am positive that if I knew how to create a record, I would be able to update one too.
app.post('/process_form_update_airports', function(req, res){

    var airportcode = req.body.airportcode2
    var airportname = req.body.airportname2
    var country = req.body.country2

   console.log("Successfully completed");
   axios.post('http://127.0.0.1:5000/api/airports')
   .then((response)=>{
        let airports = {"airportcode": airportcode, "airportname": airportname, "country": country};
        response.put(airports);
        console.log(airports);
        res.render('pages/airports', {
            airports: airports
       });
    })
})


// API to get planes. These API's are the reason I have had so much trouble with this project. 
// I can get the data but I do not know how to store the data. I have tried the methods used in the 
// homeworks and exam 2 but they have failed. I tried some of the methods used in the in-class 
// examples and those also failed. I know I am close but I have not been able to GET the planes.
app.get('/planes', function(req, res) {

    //local API call to my Python API that holds planes
    axios.get(`http://127.0.0.1:5000/api/planes`)
    .then((response)=>{
        var planes = response.data[0]
        var tagline = "Hello, These are your current planes!";
        console.log(planes);
         // use res.render to load up planes page
        res.render('pages/planes', {
            planes: planes,
            tagline: tagline
        });
    }); 
});


// this is where planes are deleted at. the parsed model is added as the search token and the API and backend execute the operation.
// NOTE: The server does not crash with the function error. The backend executes the delete in the mySQL database. 
// all that has to be done is to go back and refresh the page. The record will be deleted and the GET will be updated.
app.post('/process_form_del_planes', function(req, res){
    // create a variable to hold the model input
    var model = req.body.model1

   console.log("Deleted: " + model);
   axios.delete('http://127.0.0.1:5000/api/planes?model='+model)
   .then((response)=>{
       let planes = response.data;
       console.log(planes);
       res.render('pages/planes', {
           planes: planes
       });
    })
})


// this is where planes are added. I have not been able to get this operation to work. I have spent 
// the last two days trying to get the POST to work but I have exhausted all ideas and there are 
// absolutely zero resources online. If you could please fix one of my POST operations where I am 
// to create a record, I would GREATLY appreciate it. I just can’t figure out what I am doing wrong. 
// I am positive that if I knew how to create a record, I would be able to update one too.
app.post('/process_form_planes', function(req, res){

    var make = req.body.make
    var model = req.body.model
    var year = req.body.year
    var capacity = req.body.capacity

   console.log("Successfully completed");
   axios.post('http://127.0.0.1:5000/api/planes')
   .then((response)=>{
        let planes = {"make": make, "model": model, "year": year, "capacity": capacity}
        console.log(planes);
        response.post(planes);
        res.render('pages/planes', {
            planes: planes,
       });
    })
})


// this is where planes are updatedd. I have not been able to get this operation to work. I have spent 
// the last two days trying to get the POST to work but I have exhausted all ideas and there are 
// absolutely zero resources online. If you could please fix one of my POST operations where I am 
// to create a record, I would GREATLY appreciate it. I just can’t figure out what I am doing wrong. 
// I am positive that if I knew how to create a record, I would be able to update one too.
app.post('/process_form_update_planes', function(req, res){

    var make = req.body.make2
    var model = req.body.model2
    var year = req.body.year2
    var capacity = req.body.capacity2

   console.log("Successfully completed");
   axios.post('http://127.0.0.1:5000/api/planes')
   .then((response)=>{
        let planes = {"make": make, "model": model, "year": year, "capacity": capacity}
        console.log(planes);
        response.put(planes);
        res.render('pages/planes', {
            planes: planes,
       });
    })
})


app.get('/', function(req, res) {
    // this will render the login spage 
    res.render("pages/login.ejs");
});


// process_form used for log in authentifacation. I did not get to perfect the login. THe user name is username and the password is password.
// I included what I was trying to do commented out.
app.post('/process_form_login', function(req, res){
    // create a variable to hold the username parsed from the request body
    var username = req.body.username
    // create a variable to hold password input
    var password = req.body.password

    
    console.log("username is: " + username);
    console.log("password is: " + password);
    if(password === 'password')
    {
        res.render('pages/flights', {
            username: username,
            auth: true
        });
    }
    let sentence = 'http://127.0.0.1:5000/api/login?username='+username;
    let newsentence = sentence+'&password='+password;
    console.log(newsentence);
     /*    
    axios.get(newsentence)
    .then((response)=>{
        let musicData = response.data;
        console.log(musicData);
        if(password === "password")
        {
            res.render('pages/flights', {
                musicData: musicData,
                auth: true
            });
        }
        else
        {
            res.render('pages/login', {
                musicData: 'UNAUTHORIZED',
                auth: false
            });
        }
    })  */
})
    

app.get('/login', function(req, res) {
    res.render("pages/login");
});


app.listen(8080);
console.log('8080 is the magic port');
