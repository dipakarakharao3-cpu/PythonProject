# Base class
class Vehicle:
    def __init__(self, make, model):
        self.make = make  # Attribute for the manufacturer of the vehicle
        self.model = model  # Attribute for the model of the vehicle

    def info(self):
        return f"Vehicle: {self.make} {self.model}"  # Method to return vehicle information

# Derived class
class Car(Vehicle):
    def __init__(self, make, model, year):
        # Call the constructor of the base class to initialize make and model
        super().__init__(make, model)
        self.year = year  # Additional attribute for the year of manufacture

    def info(self):
        # Call the info method of the base class and extend it to include the year
        return f"{super().info()} ({self.year})"

# Creating an instance of Car
car = Car("Mercedes-Benz", "C 300 Coupe 2D", 2018)

# Calling the info method on the Car instance
print(car.make)  # Output: Vehicle: Mercedes-Benz C 300 Coupe 2D (2018)
