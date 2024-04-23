#!/usr/bin/node

// prints 3 lines using array of strings and loop

const args = process.argv;
const langs = ["C is fun", "Python is cool", "Javascript is amazing"];
for (let i = 0; i < langs.length; i++) {
    console.log(langs[i]);
}
