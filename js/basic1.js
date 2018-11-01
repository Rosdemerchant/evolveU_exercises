console.log("Hello world from js file");

var counter = 0;

function addTwo() {
var a = parseInt(document.getElementById("txt1").value);
var b = parseInt(document.getElementById("txt2").value);
var sum = a + b;
	console.log(sum)

}

function xyCirc() {
var x = document.getElementById("cx").value;
var y =	document.getElementById("cy").value;
var circ = document.getElementById("circle");
circ.setAttribute('cx', x);
circ.setAttribute('cy', y);
}
function myFunction() {
	console.log("I am in myFunction");
}

function myMouse() {
	console.log("I am in myMouse");	
}
function myAppend() {
	counter = counter + 1;
//	counter += 1;
//	counter++;
	var div =document.getElementById("mydiv");
	div.innerHTML += 'adding more stuff #' + counter + '</br>';

}
function clearFunc() {
	var div =document.getElementById("mydiv");
	div.innerHTML =  "";

}

function movecircle() {
	var div = document.getElementById("circle");
	div.setAttribute('transform','translateY(10px)');
	//div.setAttribute('cx', 81);
	//div.setAttribute('cy', 81);
	
}

// function moverect() {
// 	var div = document.getElementById("rect");
// 	div.setAttribute();
// 	div.setAttribute();
// }
