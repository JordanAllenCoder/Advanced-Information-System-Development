// load the things we need
var express = require('express');
var app = express();
const bodyParser  = require('body-parser');

// required module to make calls to a REST API
const axios = require('axios');

app.use(bodyParser.urlencoded());

// set the view engine to ejs
app.set('view engine', 'ejs');

// use res.render to load up an ejs view file

// choose the default API
app.get('/', function(req, res) {

    //itunes API call
    axios.get('https://randomuser.me/api/')
    .then((response)=>{
        let musicData = response.data;
        console.log(musicData);
        res.render('pages/choose', {
            music: musicData
        });
    });

}); 
// this API is used to get the random user in which I will parse for the requested information.
// every time I changed music to user on either the js or ejs file it would crash the code. I am not sure why.
// w3 schools helped me navigate the options I had with the bootstrap. It was very informative and helpful.

app.listen(8080);
console.log('8080 is the magic port');
