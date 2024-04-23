#!/usr/bin/node
// prints 'c is fun'

const args = process.argv;
if (args.length < 2) {
    console.log("Missing number of occurrences");
} else {
    const num = parseInt(args[2]);
    if (isNaN(num)) {
        console.log("Missing number of occurrences");
    } else {
        for (let i = 0; i < num; i++) {
            console.log("C is fun");
        }
    }
}
