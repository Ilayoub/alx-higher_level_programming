#!/usr/bin/node
// The function that increments and calls a function

exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
