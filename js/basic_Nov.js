// var moveTop = function() {
// 	var myButton = 'Move to Top'
// }
// ()

/*var myTop = (function() {


var text = document.getElementbyID('.top').value;


*/




var myModule = (function() {

	document.querySelector('.divbuilder').addEventListener('click', function() {
	var div = document.createElement('DIV'); 
	var insertDiv = document.querySelector('.divcontainer').appendChild(div);
	insertDiv.classList.add('adddiv');
	var node = document.createTextNode("");

	//var element = document.getElementById("div1");
	//para.appendChild(node);
	//list.removeChild(list.childNodes[0]);  
	var element = document.getElementById(div);
    element.parentNode.removeChild(adddiv);

});


	var printJas = function(arr) {
	for(i in arr) { console.log (i +' :' +arr[i]) }
		Array.isArray
	}


	document.querySelector('.printobject').addEventListener('click', function() {
		//for(i in printobject) { console.log (i +' :' +printobject[i]) }
			var text = document.querySelector('.text').value;
			var myJas = JSON.parse(text);
			var newArray = Array.isArray(myJas);
			console.log(newArray);

	});
	// var myString = 'My Value';
	// console.log('hello world');

	document.querySelector('.btn').addEventListener('click', function() {

	var text = document.querySelector('.text').value;
		var bottom = document.querySelector('.bottom');
		bottom.innerHTML = text;
	});

	document.querySelector('.jsonbutton').addEventListener('click', function() {
		var text = document.querySelector('.text').value;
		var myJas = JSON.parse(text);
		console.log();
	
	printJas(myJas);
	
	});

	document.querySelector('.printarray').addEventListener('click', function() {
		for (var i=0; i <myArray.length; i++) {
				console.log(myArray[i] + ':' + i);
		}

	})
	
	var myArray = [1,2,3,4,5,6,7];	
		var myObject = { 
			name : 'ros',
			job: 'teacher',
			city: 'Calgary'
		}
	
		})();
	// document.querySelector('.printobject').addEventListener('click', function() {
	// 	for(i in myObject) { console.log (i +' :' +myObject[i]) }
			
	// 		});

	// });
		



	// function myFunc() {
	// 	console.log('I am in myFunc');

	// }
	
	// return {
	// 	stuff : 'Some Stuff',
	// 	yourFunc: myFunc
	// };
	// document.querySelector('.btn').addEventListener('click', function() {

	// 	var text = document.querySelector('.text').value;
	// 	var bottom = document.querySelector('.bottom');
	// 	bottom.innerHTML = text;
	// });
	
//})();
// console.log(myModule);
// myModule.yourFunc();
// //console.log(myModule.MyString);
// function myprint() {
// 		console.log('Hello World...')
// 	}
// myprint();
