<file_path>
python_stuff/Basics/OOPs.py
</file_path>

<edit_description>
Integrate the makeup example from Question.py into OOPs.py as a new section explaining class variables vs instance variables, while keeping the progressive structure.
</edit_description>

# Object-Oriented Programming (OOP) in Python - Progressive Guide
# This file starts with basic examples using a Car class, then builds up OOP concepts step by step.
# Finally, it applies these concepts to real-life scenarios in Machine Learning (ML) and Backend development.

# 1. BASIC CLASS AND OBJECT (Starting with Car)
# A class is a blueprint. An object is an instance of the class.

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print(f"{self.color} {self.brand} is starting...")


# Creating objects
car1 = Car("Tesla", "Red")
car2 = Car("BMW", "Black")
car1.start()  # Output: Red Tesla is starting...
car2.start()  # Output: Black BMW is starting...


# 1.5 CLASS VARIABLES VS INSTANCE VARIABLES (Using Makeup Example)
# Class variables are shared by all instances of the class. Instance variables are unique to each object.
# Modifying a class variable affects all instances, unless overridden by an instance variable.

class make_up:
    tax_amt = 0.18  # Class variable: shared by all instances

    def __init__(self, first, last, product, price):
        self.first = first  # Instance variable
        self.last = last    # Instance variable
        self.product = product  # Instance variable
        self.price = price  # Instance variable
        self.email = first + "." + last + "@makeup.com"  # Instance variable

    def full_name(self):
        return f"{self.first} {self.last}"


# Creating an object
person1 = make_up("Khushi", "Sharma", "Lipstick", 500)
person1.tax_amt = 45  # This creates an instance variable, overriding the class variable for this object

print(person1.full_name())  # Output: Khushi Sharma
print(person1.email)  # Output: Khushi.Sharma@makeup.com
print(person1.product)  # Output: Lipstick
print(person1.price)  # Output: 500
print(person1.tax_amt)  # Output: 45 (instance variable)
print("Final Price:", person1.price + (person1.price * make_up.tax_amt))  # Uses class variable 0.18

# Uncomment below to see class variable behavior
# person2 = make_up("Kirti", "Singh", "Foundation", 1000)
# print(person2.full_name())  # Output: Kirti Singh
# print(person2.email)  # Output: Kirti.Singh@makeup.com
# print(person2.product)  # Output: Foundation
# print(person2.price)  # Output: 1000
# print(make_up.tax_amt)  # Output: 0.18 (class variable unchanged)
# print("Final Price:", person2.price + (person2.price * make_up.tax_amt))  # Output: Final Price: 1180.0


# 2. ADDING ENCAPSULATION (Hiding data in Car)
# Encapsulation bundles data and restricts access using private attributes (with __).
class Car:
    def __init__(self, brand, color, fuel_level):
        self.brand = brand
        self.color = color
        self.__fuel_level = fuel_level  # Private attribute

    def start(self):
        if self.__fuel_level > 0:
            print(f"{self.color} {self.brand} is starting...")
        else:
            print(f"{self.color} {self.brand} has no fuel!")

    def refuel(self, amount):
        self.__fuel_level += amount
        print(f"Refueled {self.brand} by {amount}. Fuel level: {self.__fuel_level}")


car3 = Car("Toyota", "Blue", 50)
car3.start()  # Output: Blue Toyota is starting...
car3.refuel(20)  # Output: Refueled Toyota by 20. Fuel level: 70
# car3.__fuel_level  # This would error due to encapsulation


# 3. ADDING INHERITANCE (Extending Car)
# Inheritance allows a child class to reuse parent class features.
class ElectricCar(Car):  # Inherits from Car
    def __init__(self, brand, color, battery_level):
        super().__init__(
            brand, color, 0
        )  # Call parent constructor (fuel_level not used)
        self.battery_level = battery_level

    def charge(self, amount):
        self.battery_level += amount
        print(f"Charged {self.brand} by {amount}. Battery: {self.battery_level}%")

    def start(self):  # Overriding parent method
        if self.battery_level > 10:
            print(f"{self.color} {self.brand} (Electric) is starting silently...")
        else:
            print(f"{self.color} {self.brand} needs charging!")


e_car = ElectricCar("Tesla", "White", 80)
e_car.start()  # Output: White Tesla (Electric) is starting silently...
e_car.charge(20)  # Output: Charged Tesla by 20. Battery: 100%


# 4. ADDING POLYMORPHISM (Different behaviors for same method)
# Polymorphism allows the same method name to behave differently.
def test_drive(vehicle):
    vehicle.start()  # Same method, different behavior based on object type


test_drive(car3)  # Regular car: Blue Toyota is starting...
test_drive(e_car)  # Electric car: White Tesla (Electric) is starting silently...

# 5. ADDING ABSTRACTION (Hiding complexity with abstract classes)
# Abstraction defines interfaces without implementation details.
from abc import ABC, abstractmethod


class Vehicle(ABC):  # Abstract base class
    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("Car moves on roads")


class Bike(Vehicle):
    def move(self):
        print("Bike moves on roads or trails")


vehicles = [Car(), Bike()]
for v in vehicles:
    v.move()  # Abstraction: Focus on 'move' without knowing details

# 6. REAL-LIFE EXAMPLES FROM ML AND BACKEND
# Applying OOP concepts to ML (Machine Learning) and Backend scenarios.


# ML Example: Inheritance and Polymorphism for Models
class MLModel(ABC):
    @abstractmethod
    def train(self, data):
        pass

    @abstractmethod
    def predict(self, input_data):
        pass


class NeuralNetwork(MLModel):
    def train(self, data):
        print(f"Training NeuralNetwork on {data}")

    def predict(self, input_data):
        return f"NeuralNetwork predicts: {input_data} classified"


class DecisionTree(MLModel):
    def train(self, data):
        print(f"Training DecisionTree on {data}")

    def predict(self, input_data):
        return f"DecisionTree predicts: {input_data} categorized"


models = [NeuralNetwork(), DecisionTree()]
for model in models:
    model.train("dataset")  # Polymorphism
    print(model.predict("new sample"))


# Backend Example: Encapsulation and Inheritance for API Services
class APIService:
    def __init__(self, endpoint):
        self.__endpoint = endpoint  # Encapsulated

    def get_data(self):
        return f"Fetching from {self.__endpoint}"


class UserService(APIService):
    def __init__(self, endpoint):
        super().__init__(endpoint)

    def create_user(self, user_data):
        print(f"Creating user: {user_data} via {self.get_data()}")


user_svc = UserService("/api/users")
user_svc.create_user({"name": "Alice", "email": "alice@example.com"})

# This progressive structure shows how OOP builds from basics to advanced, real-world applications.
