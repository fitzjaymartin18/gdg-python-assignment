class Car:
    # Initializing the value
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Function that describes the car
    def describe(self):
        return f"This car is {self.year} {self.make} {self.model}."
    
# Creating an instance
car = Car("Ford", "Raptor F-150s", "2024")

# Printing the result
print(car.describe())
