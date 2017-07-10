var fs = require("fs");    
var mongoose = require('mongoose');                                     
var lineReader = require('readline').createInterface({
  input: require('fs').createReadStream('myersBriggsQuestions.txt')
});

lineReader.on('line', function (line) {   
	conn
	// insert line into db;
});