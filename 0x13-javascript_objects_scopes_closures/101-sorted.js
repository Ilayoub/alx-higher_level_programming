#!/usr/bin/node
// The function imports a dictionary of occurrences by user
// id and computes a dictionary of user ids by occurrence

const dictInput = require('./101-data').dict;
const outDict = {};

for (const key in dictInput) {
  const ocurr = dictInput[key];
  outDict[ocurr] = [];
  for (const keys in dictInput) {
    if (dictInput[keys] === ocurr) {
      outDict[ocurr].push(keys);
    }
  }
}
console.log(outDict);
