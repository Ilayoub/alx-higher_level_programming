#!/usr/bin/node
// The function returns the reversed version of a list

exports.esrever = function (list) {
  return list.reduceRight(function (array, current) {
    array.push(current);
    return array;
  }, []);
};
