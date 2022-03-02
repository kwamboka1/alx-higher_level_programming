#!/usr/bin/node

let no_arg = 0;

exports.logMe = function (item) {
  console.log(no_arg + ': ' + item);
  no_arg++;
};
