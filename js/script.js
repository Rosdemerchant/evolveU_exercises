/*************************
*Variables and data types

var firstName = 'John';
console.log(firstName);

var lastName = 'Smith';
var age = 28;

var fullAge = true;
console.log(fullAge);

var job;
console.log(job);

job = 'Teacher';
console.log(job);

/************************
*Variable mutation and type coercion
*
var firstName = 'John';
var age = 28;
Type coercion
console.log(firstName + ' ' + age)

var job, isMarried;
job = 'teacher';
isMarried = false;

console.log(firstName + ' is a ' + age + ' year old ' + job + '. Is he married? ' +isMarried);

//Variable mutation
age = 'twenty eight';
job = 'driver';

alert(firstName + ' is a ' + age + ' year old ' + job + '. Is he married? ' +isMarried);

var lastName = prompt('What is his last Name?');
console.log(firstName + ' ' + lastName);


Basic Operators

var year, yearJohn, yearMark;
now = 2018;
ageJohn = 28;
ageMark = 33;

Math Operators
yearJohn = now - ageJohn;
yearMark = now - ageMark;

console.log(yearJohn);
console.log(now + 2);
console.log(now / 10);

// Logical operators
var johnOlder = ageJohn < ageMark;
console.log(johnOlder);

typeof operator
console.log(typeof johnOlder);
console.log(typeof ageJohn);
console.log(typeof 'Mark is older than John');
var x;
console.log(typeof x);

/***************************
*Operator precedence
*

var now = 2018;
var yearJohn = 1989;
var fullAge = 18;

// Multiple operators
var isFullAge = now - yearJohn >= fullAge; // true
console.log(isFullAge);

//Grouping
var ageJohn = now - yearJohn;
var ageMark = 35;
var average = (ageJohn + ageMark) / 2;
console.log(average);

//multiple assignments
var x, y;
x = y = (3 + 5) * 4 - 6;// 8 * 4 - 6 // 32 - 6 // 26
console.log(x, y);

// More operators
x *= 2;
console.log(x);
x += 10;
console.log(x);
x = x + 1;
x += 1;
x--;
console.log(x);

/********************************
* If / else statements
*
var firstName = 'John';
var civilStatus = 'married';

var isMarried = true;
if (isMarried) {
	console.log(firstName + ' is married!');
} else {
	console.log(firstName + ' will hopefully marry soon :)');
}

****************************
* Boolean logic

var firstName = 'John';
var age = 20;

if (age < 13) { 
	console.log(firstName + ' is a boy.');
} else if (age >= 13 && age < 20) { 
	{console.log(firstName + ' is a teenager.');}
} else if (age >= 20 && age < 30) {
	console.log(firstName + ' is a young man.');
} else {
	console.log(firstName + ' is a man.');
} 

function golfScore(par, strokes) {
  // Only change code below this line
  if (strokes == 1){
    return "Hole-in-one!";
  } else if (strokes <= par -2){
    return "Eagle";
  } else if (strokes == par -1) {
    return "Birdie";
  } else if (strokes == par) {
    return "Par";
  } else if (strokes == par +1) {
    return "Bogey";
  } else if (strokes == par +2) {
    return "Double Bogey";
  } else {
    return "Go Home!";
  }
  // Only change code above this line
}
// Change these values to test
golfScore(5, 4);

function caseInSwitch(val) {
  var answer = "";
  switch(val) {
    case 1:
      return "alpha";
      break;
    case 2:
      return "beta";
      break;
    case 3:
      return "gamma";
      break;
    case 4:
      return "delta";
      break;
  }
}
/*************************
* The Ternary Operator and Switch Statements

var firstName = 'John';
var age = 14;

age >= 18 ? console.log(firstName + ' drinks beer.')
: console.log(firstName + ' drinks juice.');

var drink = age >= 18 ? 'beer' : 'juice';
/****************************************
*Switch Statement*/
/*var firstName = 'John';
var job = "instructor";
switch (job) {
  case 'teacher':
  case 'instructor':
    console.log(firstName + ' teaches kids how to code.');
    break;
  case 'driver':
    console.log(firstName + ' drives an uber in Lisbon.');
    break;
  case 'designer':
    console.log(firstName + ' designs beautiful websites.');
    break;
  default:
    console.log(firstName + ' does something else.');
}
age = 22;
switch (true) {
  case age < 13:
    console.log(firstName + ' is a boy.');
    break;
  case age >= 13 && age < 20:
  console.log(firstName + ' is a teenager.');
    break;
  case age >= 20 && age < 30:
  console.log(firstName + ' is a young man.');
  break;
  default: 
  console.log(FirstName + ' is a man.');
}

function switchOfStuff(val) {
  var answer = "";
  
  switch(val){
    case 'a': answer = 'apple'; 
    break;
    case 'b': answer = 'bird'; 
    break;
    case 'c': answer = 'cat'; 
    break;
    default: answer = 'stuff';
  }
  
  return answer;  
}
/***********************************
* Truthy and Falsy values and equality operators
*/

// falsy values: undefined, null, 0, '', NaN
//truthy values: NOT falsy values

/*var height;
height = 23;
if (height || height === 0) {
  console.log('Variable is defined');
} else {
  console.log('Variable has NOT been defined');

}
//Equality operators
if (height == '23') {
  console.log('The == operator does type coercion!');
}
// Modify the function abTest so that if a or b are less than 0 the function will immediately exit with a value of undefined.

// function abTest(a, b) {
  
//  if (a < 0 || b < 0) {
//    return "undefined";
//  }  
//*******************************function cc(card) {
/*switch(card){
        case 2:
        case 3:
        case 4:
        case 5:
        case 6:
          count++;
          break;
        case 10:
        case "J":
        case "Q":
        case "K":
        case "A":
          count--;
          break;
      }
      if (count > 0){
        return count + " Bet";
      } else {
        return count + " Hold";
      }
    }

    Code Explanation:
Check the value of each card via a switch statement.
The variable count:

Increases by 1 if the card is a 2, 3, 4, 5, or 6.
Since 7, 8, and 9 aren’t worth anything, we ignore those cards in our switch statement.
Decreases by 1 if the card is a 10, ‘J’, ‘Q’, ‘K’, or ‘A’.
Check the value of count and return the appropriate response.
Example Run

cc(2); runs.
The switch statement hits case 2, jumps down and adds 1 to the variable count.
The switch statement then hits the break and cc(3); runs.
This cycle continues until the final call is made, cc('A');.
After the switch statement, the if statement checks count, which is now 0.
This then drops down to the else statement, which will return 0 Hold.
Note: As mentioned earlier, the switch statement could have also been an else if statement.