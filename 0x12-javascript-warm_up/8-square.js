#!/usr/bin/node

const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0, side; i < size; i++) {
    side = '';
    for (let j = 0; j < size; j++) {
      side += 'X';
    }
    console.log(side);
  }
}
