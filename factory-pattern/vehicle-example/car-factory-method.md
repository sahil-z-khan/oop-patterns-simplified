# Vehicle Factory Example

This project demonstrates a **Factory Method Design Pattern** for creating a `Vehicle` object. Here, we use a `VehicleFactory` to instantiate a specific `Vehicle` type—in this case, a `Honda` vehicle.

The Factory Method pattern allows the client to interact with a factory to create an instance of a `Vehicle` without needing to know the specifics of the `Vehicle` class. This makes the code more modular and adaptable for future extensions, such as adding more vehicle types.

## Table of Contents

1. [Overview](#overview)
2. [Classes and Components](#classes-and-components)
3. [Usage](#usage)
4. [Extending the Pattern](#extending-the-pattern)

---

## Overview

This code implements a simplified **Factory Method pattern**:
- **Product**: `Vehicle`, an abstract class that declares a method for vehicle behavior (`rev_vehicle`).
- **Concrete Product**: `Honda`, a class that represents a specific type of `Vehicle`.
- **Factory**: `VehicleFactory`, an abstract factory interface that declares a method for creating vehicles.
- **Concrete Factory**: `HondaFactory`, a specific factory that creates `Honda` vehicles.

### Pattern Flow
The client code interacts only with the factory (i.e., `HondaFactory`) to get a `Honda` vehicle. This encapsulation allows the client to remain decoupled from the specific `Vehicle` types.

---

## Classes and Components

### 1. Product: `Vehicle`

`Vehicle` is an abstract class representing a general vehicle. It includes an abstract method, `rev_vehicle`, which each specific vehicle class will implement:
```python
class Vehicle:
    @abstractmethod
    def rev_vehicle(self):
        pass
```

### 2. Concrete Product: `Honda`

`Honda` is a specific implementation of `Vehicle`, representing a Honda vehicle. It provides a concrete implementation of `rev_vehicle`:
```python
class Honda(Vehicle):
    def rev_vehicle(self):
        return "vrooommmm - by honda"
```

### 3. Factory: `VehicleFactory`

`VehicleFactory` is an abstract class that declares the `create_vehicle` method, which must be implemented by any concrete factory subclass. This method is responsible for creating a `Vehicle` instance:
```python
class VehicleFactory:
    @abstractmethod
    def create_vehicle(self):
        pass
```

### 4. Concrete Factory: `HondaFactory`

`HondaFactory` is a specific implementation of `VehicleFactory`. Its `create_vehicle` method returns an instance of `Honda`, encapsulating the creation process for Honda vehicles:
```python
class HondaFactory(VehicleFactory):
    def create_vehicle(self):
        return Honda()
```

---

## Usage

The following code demonstrates how to use the factory to create a `Honda` vehicle and access its behavior:

```python
if __name__ == "__main__":
    my_honda = HondaFactory()  # Create the factory
    honda_vehicle: Honda = my_honda.create_vehicle()  # Use the factory to create a Honda vehicle

    print(honda_vehicle.rev_vehicle())  # Utilize the Honda vehicle's rev method
```

### Output
```plaintext
vrooommmm - by honda
```

### Explanation

- `HondaFactory` is instantiated to create the `my_honda` factory.
- The factory’s `create_vehicle` method is called, which returns a `Honda` instance (`honda_vehicle`).
- The `rev_vehicle` method of `honda_vehicle` is then called, producing the output `"vrooommmm - by honda"`.

---

## Extending the Pattern

To add more vehicle types, such as `Toyota` or `Ford`:

1. **Create a new Concrete Product**: Define a class like `Toyota` or `Ford` that implements `Vehicle`.
2. **Create a new Concrete Factory**: Define a factory class, such as `ToyotaFactory` or `FordFactory`, that returns an instance of the new vehicle.
3. **Use the New Factory**: In the client code, you can then instantiate and use the new factory to create and interact with the new vehicle type.

This design makes it easy to introduce new types of vehicles without modifying existing code, following the **Open/Closed Principle**—open for extension, closed for modification.