#!/usr/bin/node
// The function prints message depending of the number of arguments

const count = process.argv.length;
console.log(count === 2 ? 'No argument' : count === 3 ? 'Argument found' : 'Arguments found');
