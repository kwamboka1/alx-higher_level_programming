#!/usr/bin/node

const arg = process.argv;
const requestURL = arg[2];
const req = require('request');
req(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const listFilms = (JSON.parse(body).results);
    let count = 0;
    for (let i = 0; i < listFilms.length; i++) {
      for (let j = 0; j < listFilms[i].characters.length; j++) {
        if (listFilms[i].characters[j].includes('/18/')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
