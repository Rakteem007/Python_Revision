class Car:

    total_car=0

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car += 1
    
    def get_brand(self):
        return self.__brand
    
    def display(self):
        return f"{self.__brand} --> {self.__model}"
    
    # polymorphism --> refer to the Inheritence.py file
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "this is a car.\nThis is a mean of transport"
    
    # makes this method access as property. 
    @property
    def model(self):
        return self.__model

car1 = Car("Mercedes Benz", "GL clas S")
# print(car1.brand, car1.model)
# print(car1.display())

car2=Car("Audi", "Elite Class")
# print(car2.brand, car2.model)

# encapsulation
# print(car1.fuel_type())
# print(f"the total number of cars is {Car.total_car}")

# print(Car.general_description())

print(car2.model)

print(isinstance(car2, Car));