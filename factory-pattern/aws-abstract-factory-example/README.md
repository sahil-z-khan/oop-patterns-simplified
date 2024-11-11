# AWS Service Factory Method Pattern

This project demonstrates the **Factory Method Design Pattern** for managing different AWS services. It allows for the creation of AWS service instances dynamically and performs actions such as starting, stopping, and retrieving ARNs (Amazon Resource Names) for each service.

The pattern separates the creation logic of AWS services (EC2, RDS, ECS) from the client code. This setup enables flexibility and scalability, making it easier to add or modify services.

## Table of Contents

1. [Structure](#structure)
2. [Classes and Components](#classes-and-components)
3. [Usage](#usage)
4. [How It Works](#how-it-works)
5. [Extending the Pattern](#extending-the-pattern)

---

## Structure

The code is structured as follows:

- **Enum**: Defines different service types (`ServiceType`).
- **Abstract Product (`AWSService`)**: Defines the interface that all AWS services implement.
- **Concrete Products**: Implementations of AWS services, such as `EC2Service`, `RDSService`, and `ECSService`.
- **Abstract Factory (`AWSServiceCreator`)**: Declares the factory method `create_service`.
- **Concrete Factories**: Specific factories for each service type, such as `EC2Creator`, `RDSCreator`, and `ECSCreator`.
- **Client Code**: Uses a dictionary to map service types to factories, allowing dynamic selection of services and actions.

---

## Classes and Components

### 1. Enum: `ServiceType`

The `ServiceType` enum defines constants for each AWS service:
```python
class ServiceType(Enum):
    EC2 = 1
    RDS = 2
    ECS = 3
```

### 2. Abstract Product: `AWSService`

`AWSService` defines an interface that all AWS service implementations must follow:
- `start`: Starts the service.
- `stop`: Stops the service.
- `get_service_arn`: Returns the service ARN.

```python
class AWSService(ABC):
    @abstractmethod
    def start(self) -> str: pass

    @abstractmethod
    def stop(self) -> str: pass

    @abstractmethod
    def get_service_arn(self) -> str: pass
```

### 3. Concrete Products

Each AWS service (EC2, RDS, ECS) implements the `AWSService` interface:
- **`EC2Service`**: Implements methods specific to EC2 instances.
- **`RDSService`**: Implements methods specific to RDS databases.
- **`ECSService`**: Implements methods specific to ECS clusters.

For example:
```python
class EC2Service(AWSService):
    def start(self) -> str:
        return "Starting EC2 instance"
    def stop(self) -> str:
        return "Stopping EC2 instance"
    def get_service_arn(self) -> str:
        return "arn:aws:ec2:region:account-id:instance/instance-id"
```

### 4. Abstract Factory: `AWSServiceCreator`

The `AWSServiceCreator` class is an abstract factory that declares a factory method, `create_service`, to be implemented by its subclasses:
```python
class AWSServiceCreator(ABC):
    @abstractmethod
    def create_service(self) -> AWSService: pass

    def manage_service(self, action: str) -> None:
        service = self.create_service()
        if action == "start":
            print(service.start())
        elif action == "stop":
            print(service.stop())
        elif action == "arn":
            print(service.get_service_arn())
        else:
            print("Unknown action")
```

### 5. Concrete Factories

Each concrete factory (`EC2Creator`, `RDSCreator`, `ECSCreator`) overrides `create_service` to produce the correct AWS service instance:
```python
class EC2Creator(AWSServiceCreator):
    def create_service(self) -> AWSService:
        return EC2Service()
```

### 6. Client Code

The `manage_aws_service` function acts as the client, using a dictionary to map `ServiceType` values to their corresponding factories. This setup allows for easy addition or modification of services:
```python
def manage_aws_service(service_type: ServiceType, action: str):
    creator_mapping = {
        ServiceType.EC2: EC2Creator(),
        ServiceType.RDS: RDSCreator(),
        ServiceType.ECS: ECSCreator()
    }
    creator = creator_mapping.get(service_type)
    if creator:
        creator.manage_service(action)
    else:
        print("Unknown service type")
```

---

## Usage

The following examples show how to use the `manage_aws_service` function to interact with different AWS services:

```python
manage_aws_service(ServiceType.EC2, "start")
# Output: Starting EC2 instance

manage_aws_service(ServiceType.RDS, "stop")
# Output: Stopping RDS database

manage_aws_service(ServiceType.ECS, "arn")
# Output: arn:aws:ecs:region:account-id:cluster/cluster-name
```

## How It Works

1. **Client Code Calls `manage_aws_service`**: This function takes a `ServiceType` and an `action`.
2. **Factory Selection**: The `creator_mapping` dictionary maps each `ServiceType` to a factory class (`EC2Creator`, `RDSCreator`, or `ECSCreator`).
3. **Service Creation and Action Execution**:
   - `manage_service` is called on the selected factory, which creates the specified AWS service instance.
   - Depending on the `action`, the service instance’s `start`, `stop`, or `get_service_arn` method is invoked.

---

## Extending the Pattern

To add a new AWS service, such as **S3**:

1. Create a new concrete product (e.g., `S3Service`) that implements `AWSService`.
2. Implement a corresponding concrete factory (e.g., `S3Creator`) that inherits from `AWSServiceCreator` and returns an `S3Service` instance.
3. Add the new service type to the `ServiceType` enum.
4. Update `creator_mapping` in `manage_aws_service` to include the new service and factory.

This approach keeps the code flexible and easily extendable.
