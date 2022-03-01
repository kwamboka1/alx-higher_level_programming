#!/usr/bin/node

const count = parseInt(process.argv[2]);

// Check if argument is NaN

if (isNaN(count)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < count; i++) {
    console.log('C is fun');
  }
}
