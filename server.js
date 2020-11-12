const http = require('http');
const express = require('express');
const path = require('path');
const app = express();
app.use(express.json());
app.use(express.static(path.join(__dirname, 'src')));
// default URL for website
app.use('/', function(req,res){
  res.sendFile(path.join(__dirname + '/src/index.html'));
});
app.use('/all-datasets-iframe', function(req, res){
  res.sendFile(path.join(__dirname + '/src/test.html'));
});
const server = http.createServer(app);
const port = 3000;
server.listen(port);
console.debug('Server listening on port ' + port);