/*******************
* CODING CHALLENGE 1


Mark and John are trying to compare their BMI, 
which is calculated using the formula:
BMI = mass / height^2 = mass / height * height = mass.
(mass in kg and height in meter).

1. Store Mark's and John's mass and height in 
variables
2. Calculate both their BMIs
3. Create a boolean variable containing information
about whether Mark has a higher BMI than John
4. Print a string to the console containing the
variable from step 3. (Something like "Is Mark's BMI
higher than John's? true").

*
***var massMark = 82;
var heightMark = 1.7;

var massJohn = 109;
var heightJohn = 1.9;

var bmiMark = massMark / (heightMark * heightMark)
var bmiJohn = massJohn / (heightJohn * heightJohn)
console.log(bmiMark, bmiJohn);

if (bmiMark > bmiJohn) {
	console.log('Mark\'s BMI is higher than John\'s.');
} else {
	console.log('John\'s BMI is higher than Mark\'s.');
}

/*******************************
* CODING CHALLENGE 2


John and Mike both play basketball in different
teams.  In the latest 3 games, John's team scored 89,
120 and 103 points, while Mike's team scored 116, 94
and 123 points.

1. Calculate the average score for each team
2. Decide which teams wins in average (hightest
average score), and print the winner to the console.
Also include the average score in the output.
3.	Then change the scores to show different winners.
Don't forget to take into account there might be a draw(the same average score) 
4. EXTRA: Mary also plays basketball, and her team
scored 97, 134 and 105 points.  Like before, log the 
average winner to the console. HINT: you will need
the && operator to take the decision.  
5. Like before, change the scores to generate 
different winners, keeping in mind there might be draws.


*/

var averageJohn = (89 + 120 + 103) / 3
var averageMike = (89 + 120 + 103) / 3
var averageMary = (97 + 134 + 105) / 3
if (averageJohn > averageMike && averageJohn ) {
	console.log("John\'s team won with a score of " + averageJohn)
	} else if (averageMike > averageJohn) {
		console.log("Mike\'s team won with a score of " + averageMike)
	} else if 
	} else {
		console.log('The game was a draw. Each team had a score of ' + averageJohn)
	}

