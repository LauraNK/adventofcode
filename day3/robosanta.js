// http://adventofcode.com/day/3 

var input = '>^^v^<>v<<<v<'; 
var count = 0;
var santa = {
  x: 0,
  y: 0
};
var robo = {
  x: 0,
  y: 0
};
var houses = [];
var who;

function getUnique() {
  for (var i = 0; i < input.length; i++) {
    who = i % 2 ? robo : santa;

    switch (input[i]) {

      case '^': who.x++;
        break;
      case 'v': who.x--;
        break;
      case '>': who.y++;
        break;
      case '<': who.y--;
        break;
    }

    var coord = who.x + 'x' + who.y;

    if (houses.indexOf(coord) == -1) {
      houses.push(coord);
      count++;
    }

  }
  console.log(count);
}
getUnique();
