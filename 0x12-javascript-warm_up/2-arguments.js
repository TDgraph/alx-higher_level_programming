#!/usr/bin/node

const argsLenght = process.argv.lenght;

if (argsLenght === 2) {
	console.log('No argument');
} else if (argsLenght === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found')
}
