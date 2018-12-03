//create a City class with four attributes on the constructor: Name, Latitude, Longitude, Population

class City extends Object {
    constructor(Name, Latitude, Longitude, Population) {
        super();
        this.Name = Name;
        this.Latitude = Latitude;
        this.Longitude = Longitude;
        this.Population = Population
    }
//create a method “show” which creates a single string with the 4 attributes 

    show() {
        return this.Name + ' ' +
        this.Latitude.toString() + ' ' +
        this.Longitude.toString() + ' ' +
        this.Population.toString()
    }
//create a method “movedIn” which receives a number that will be added to the city’s population 

    movedIn(addPeople) {
        this.Population = this.Population + addPeople;
    }
//create a method “movedOut” which receives a number that will be subtracted from the city’s population


    movedOut(delPeople) {
        this.Population = this.Population - delPeople;
    }
    //create a method “howBig” that will return one of the following:
    //City – a population > 100,000
    //Large town – a large town has a population of 20,000 to 100,000
    //Town – a town has a population of 1,000 to 20,000
    //Village – larger than a hamlet but smaller than a town
    //Hamlet – population 1 - 100
    
    howBig() {
       if (this.Population > 100000) {
            return 'City';
       } else if (this.Population >= 20000) {
            return 'Large town';
       } else if (this.Population >= 1000) {
            return 'Town';
       } else if (this.Population > 100) {
            return 'Village';
       } else {
            return 'Hamlet';
       
        }
    };
    whichSphere() {
        if (this.Latitude < 0) {
            return 'Southern Hemisphere' ;  
        } else {
            return 'Northern Hemisphere';
        }

    }
}
    //Cities =  [
     //   ('Moncton', 64.7782, 64.7782, 71890),
     //   ('Fredericton', 45.9636, 66.6431, 58220),
     //   ('Halifax', 44.6488, 63.5752, 403130),
     //   ('Saint John', 45.2733, 66.0633, 67575),
     //   ('Vernon', 50.2670, 119.2720, 40,116)
    //];
    

    //create or update a class called Community which takes no parameters
    
class Community extends Object {
    constructor() {
        super();
        this.Cities = []; 

    }
    

    addCity(Name, Latitude, Longitude, Population) {
        this.Cities.push(new City(Name, Latitude, Longitude, Population));
    }


    getPopulation() {
        let total = 0;
        for (let i in this.Cities) {
            total = total + this.Cities[i].Population;
        };
      return total;  
    }

    getMostNorthern() {
        let max = -90;
        let North = 0;
        for (let i in this.Cities) {
            if (this.Cities[i].Latitude);
            max = this.Cities[i].Latitude;
            North = i;
        }
    }

    getMostSouthern() {
        
    }
//add the following methods to Community
//addCity
//getPopulation ⇒ total for all the cities
//getMostNorthern
//getMostSouthern

}


export default{ City, Community };