#!/usr/bin/node
// The function converts a number from base 10
// to another base passed as argument

exports.converter = function (base) {
  return function (n) { return n.toString(base); };
};
