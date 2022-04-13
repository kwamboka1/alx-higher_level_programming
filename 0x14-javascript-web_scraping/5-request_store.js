#!/usr/bin/node

const args = process.argv;
const requestURL = args[2];
const fPath = args[3];
const fs = require('fs');
const req = require('request');

req(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(fPath, body, 'utf8', function (error) {
      if (error) { console.log(error); }
    });
  }
});
