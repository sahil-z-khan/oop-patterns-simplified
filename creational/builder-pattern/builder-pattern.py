class Car:
    def __init__(self, engine, wheels, color):
        self.engine = engine
        self.wheels = wheels
        self.color = color
    
    def __str__(self):
        return f"Car with {self.engine} engine, {self.wheels} wheels, and {self.color} color."

class CarBuilder:
    def __init__(self):
        self.engine = None
        self.wheels = None
        self.color = None
    
    def set_engine(self, engine):
        self.engine = engine
        return self
    
    def set_wheels(self, wheels):
        self.wheels = wheels
        return self
    
    def set_color(self, color):
        self.color = color
        return self
    
    def build(self):
        return Car(self.engine, self.wheels, self.color)

# Using the builder
builder = CarBuilder()
car = builder.set_engine("V8").set_wheels(4).set_color("red").build()
print(car)
