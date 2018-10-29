/*******************
* CODING CHALLENGE 1
* /

/*
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

*/

var massMark = 82;
var heightMark = 1.7;

var massJohn = 109;
var heightJohn = 1.9;

var bmiMark = massMark / (heightMark * heightMark)
var bmiJohn = massJohn / (heightJohn * heightJohn)
console.log(bmiMark, bmiJohn);

var ishigherMark = bmiMark > bmiJohn;
console.log('Is Mark\'s BMI higher than John\'s? ' +
ishigherMark);
