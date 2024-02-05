class Car:
    def __init__(self, make, model, year, rental_rate):
        self.make = make
        self.model = model
        self.year = year
        self.rental_rate = rental_rate
    def display_info(self):
        return f"{self.year} {self.make} {self.model} - RM{self.rental_rate} per day"
    def rental_quote(self, number_of_days):
        self.number_of_days = number_of_days
        total_rental = self.rental_rate * self.number_of_days
        return f"Total rental cost: {total_rental}"

class Sedan(Car):
    def __init__(self, make, model, year, rental_rate, num_doors):
        super().__init__(make, model, year, rental_rate)
        self.num_doors = num_doors
    def display_info(self):
        return f"{super().display_info()} with {self.num_doors} of doors."
    def rental_quote(self, number_of_days):
        return super().rental_quote(number_of_days)
    
class SUV(Car):
    def __init__(self, make, model, year, rental_rate, cargo_space):
        super().__init__(make, model, year, rental_rate)
        self.cargo_space = cargo_space
    def display_info(self):
        return f"{super().display_info()} with {self.cargo_space} of cargo space."
    def rental_quote(self, number_of_days):
        return super().rental_quote(number_of_days)

sedan = Sedan("Toyota", "Vios", 2018, 150.00, 4)
suv = SUV("Toyota", "Harrier", 2020, 200.00, 30.00)

print(sedan.display_info())
print(sedan.rental_quote(5))

print(suv.display_info())
print(suv.rental_quote(7))