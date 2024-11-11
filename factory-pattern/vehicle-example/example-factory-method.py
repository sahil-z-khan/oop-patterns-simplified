from abc import ABC, abstractmethod

# Product
class Vehicle:
    @abstractmethod
    def rev_vehicle(self):
        pass

# Concrete Product
class Honda(Vehicle):
    def rev_vehicle(self):
        return "vrooommmm - by honda"
    
# Factory
class VehicleFactory:
    @abstractmethod
    def create_vehicle(self):
        pass

# Concrete Factory
class HondaFactory(VehicleFactory):
    def create_vehicle(self):
        return Honda()
    

# Implementation
if __name__ == "__main__":
    my_honda_factory = HondaFactory() # Create the factory
    honda_vehicle: Honda = my_honda_factory.create_vehicle() # Have the factory create the "vehicle" (product)

    print(honda_vehicle.rev_vehicle()) # utilize the product

