// http://adventofcode.com/day/3 

var input = '>^^v^<>v<'; 
var notUnique = 0;
var houses = ["0x0"];

function getUnique() {
  var x = 0;
  var y = 0;
  for (var i = 0; i < input.length; i++) {

    switch (input[i]) {
      case '^': x++;
        break;
      case 'v': x--;
        break;
      case '>': y++;
        break;
      case '<': y--;
        break;
    }
    var coord = x + 'x' + y;
			
    // If in array
    if (houses.indexOf(coord) !== -1) {     
      notUnique++;
      
    } else {
      houses.push(coord);
    }

  }
	// Damn off by one errors	
  console.log(input.length - notUnique + 1);
}

getUnique();