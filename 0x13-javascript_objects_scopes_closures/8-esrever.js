#!/usr/bin/node

exports.esrever = function (list) {
  let len = list.length - 1;
  let i = 0;
  while ((len - i) > 0) {
    const idx = list[len];
    list[len] = list[i];
    list[i] = idx;
    i++;
    len--;
  }
  return list;
};
