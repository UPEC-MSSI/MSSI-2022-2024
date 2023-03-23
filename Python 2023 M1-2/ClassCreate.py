#Chaque fonction qui fait partie d'une classe = méthodes. 
#__init__ est une méthode spéciale que Python exécute automatique dès qu'on appel sa classe. 



class Dog:

#Constructeur"
    """A simple attempt to model a dog"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

#Méthodes
    def sit(self):
        """Simule a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a commande."""
        print(f"{self.name} rolled over!")


#Lorsqu'une variable de class est appelé ensuite elle devient un paramètre de la class. 
#Two type of write type (concatennation or formatage)
"""
#Création d'objet et impression des objets en utilisants la class et ses méthodes
my_dog = Dog('Cobà', 8)
print(f"My dog's name is {my_dog.name}")
print ("My dog's age is",my_dog.age," years old.")

my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Jet', 3)
print(f"\nYour dog's name is {my_dog.name}.")
print ("Your dog's age is ",my_dog.age," years old.")
your_dog.sit()

"""

class Car:
    """A simple attempt to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
"""        
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
"""

my_new_car2 = Car('audi', 'a3', 2020)
print(my_new_car2.get_descriptive_name())
my_new_car2.update_odometer()
my_new_car2.read_odometer()