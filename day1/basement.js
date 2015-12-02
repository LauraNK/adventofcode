// http://adventofcode.com/day/1

var input = '()())'; // 5
var floor = 0;

for (var i = 0; i < input.length; i++) {
	var character = input.charAt(i);
	if (character === '(') {
		floor++;
		if (floor == -1) {
			console.log(i + 1);
			break;
		}
	} 
	else if (character === ')') {
		floor--;
		if (floor == -1) {
			console.log(i + 1);
			break;
		}
				
	}	
}

