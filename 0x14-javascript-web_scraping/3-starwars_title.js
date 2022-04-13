#!/usr/bin/node

const arg = process.argv;
const movieId = arg[2];
const requestURL = 'https://swapi-api.hbtn.io/api/films/' + movieId;
const req = require('request');
req(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
