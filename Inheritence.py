from intro_classs import Car

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    # polymorphism --> refer to the intro_classes.py file
    def fuel_type(self):
        return "Electric Charge"

car = ElectricCar("Tesla", "Model S", "85kwh")
print(car.get_brand())
print(car.model)
print(car.battery_size)
print(car.fuel_type())

print(isinstance(car, ElectricCar));

