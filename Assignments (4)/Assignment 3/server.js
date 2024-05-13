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
    axios.get('https://itunes.apple.com/search?term=metallica')
    .then((response)=>{
        let musicData = response.data;
        console.log(musicData);
        res.render('pages/choose', {
            music: musicData
        });
    });

}); 
// this API is used as the starting point. It does not display any information using input.
// the left side will be used to display the music data for the artist and the right side will be used to query.

app.post('/process_form', function(req, res){
    // create a variable to hold the username parsed from the request body
    var artist = req.body.artist
    // create a variable to hold ....

   console.log("Artist/band name is: " + artist);
   axios.get('https://itunes.apple.com/search?term='+artist)
   .then((response)=>{
       let musicData = response.data;
       console.log(musicData);
       res.render('pages/choose', {
           music: musicData
       });
    })
})
// this API will be used to navigate to the correct artist.
// once the name of the artist is inserted. it is added to the search parameter and guides the API to that artist
// i imagine this was not the easiest route to take but it was the only route that I was able to get working.


app.listen(8080);
console.log('8080 is the magic port');
