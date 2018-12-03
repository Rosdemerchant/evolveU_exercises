import rd from './community';

test('test show',() => {
    let MyCity = new rd.City('Calgary', 51.0486, 114.0708, 1239000);
    expect(MyCity.show()).toBe('Calgary 51.0486 114.0708 1239000');
    MyCity = new rd.City('Vancouver', 49.2827, 123.1207, 631486);
    expect(MyCity.show()).toBe('Vancouver 49.2827 123.1207 631486');
    MyCity = new rd.City('Lima', -12.0464, 77.0428, 10000000);
    expect(MyCity.show()).toBe('Lima -12.0464 77.0428 10000000');
})

test('test movedIn',() => {
    let MyCity = new rd.City('Calgary', 51.0486, 114.0708, 1239000);
    MyCity.movedIn(10);
    expect(MyCity.show()).toBe('Calgary 51.0486 114.0708 1239010');
})

test('test movedOut',() => {
    let MyCity = new rd.City('Calgary', 51.0486, 114.0708, 1239000);
    MyCity.movedOut(10);
    expect(MyCity.show()).toBe('Calgary 51.0486 114.0708 1238990');
})

test('test whatCalled',() => {
    let MyCity = new rd.City('Calgary', 51.0486, 114.0708, 50);
    //expect(MyCity.howBig()).toBe('City');
    //expect(MyCity.howBig()).toBe('Large town');
    //expect(MyCity.howBig()).toBe('Town');
    //expect(MyCity.howBig()).toBe('Village');
    expect(MyCity.howBig()).toBe('Hamlet');
})

test('test whichSphere',() => {
    let MyCity = new rd.City('Lima', -12.0464, 77.0428, 10000000);
    expect(MyCity.whichSphere()).toBe('Southern Hemisphere');
})
//create an instance of your favorite city called myFav
let myFav = new rd.City('Honolulu', 21.3069, 157.8585, 351792);
//create a variable called c and make it = myFav
let c = myFav
console.log(c.show());
console.log(myFav.show());

//have 10000 people movedIn to your favorite city
myFav.movedIn(10000);
console.log(c.show());
console.log(myFav.show());

test('test addCity',() => {
    let x = new rd.Community();
    x.addCity('Moncton', 64.7782, 64.7782, 71890);
    expect(x.Cities[0].show()).toBe('Moncton 64.7782 64.7782 71890');
    x.addCity('Fredericton', 45.9636, 66.6431, 58220);
    expect(x.Cities[1].show()).toBe('Fredericton 45.9636 66.6431 58220');
    x.addCity('Halifax', 44.6488, 63.5752, 403130);
    expect(x.Cities[2].show()).toBe('Halifax 44.6488 63.5752 403130');
    x.addCity('Saint John', 45.2733, 66.0633, 67575);
    expect(x.Cities[3].show()).toBe('Saint John 45.2733 66.0633 67575');
    x.addCity('Vernon', 50.267, 119.272, 40.116);
    expect(x.Cities[4].show()).toBe('Vernon 50.267 119.272 40.116');

})

test('test getPopulation',() => {
    let x = new rd.Community();
    x.addCity('Moncton', 64.7782, 64.7782, 71890);
    expect(x.getPopulation()).toBe(71890);
    x.addCity('Fredericton', 45.9636, 66.6431, 58220);
    expect(x.getPopulation()).toBe(130110);
   
})

test('test getMostNorthern',() => {
    let n = North
    console.log(n);
})