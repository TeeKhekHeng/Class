class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def info(self):
        return f"{self.make} {self.model} is a vehicle."

class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make,model)
        self.year = year
    
    def info(self):
        return f"{self.make} {self.model} {self.year} is a car."
    
#Creating instances
vehicle = Vehicle("Generic", "Model")
car = Car("Toyota", "Corolla", 2022)

#Accessing methods
print(vehicle.info())
print(car.info())

