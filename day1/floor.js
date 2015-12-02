// http://adventofcode.com/day/1

var input = '(((())))()((((((((())()(()))(()'; 
var floor = 0;

for (var i = 0; i < input.length; i++) {
	if (input.charAt(i) === '(') {
		floor++;
	} 
	else if (input.charAt(i) === ')') {
		floor--;
	}	
}

console.log(floor);