from abc import ABC, abstractmethod
from enum import Enum

# Enum for AWS service types
class ServiceType(Enum):
    EC2 = 1
    RDS = 2
    ECS = 3

# Abstract Product (AWS Service Interface)
class AWSService(ABC):
    @abstractmethod
    def start(self) -> str:
        pass

    @abstractmethod
    def stop(self) -> str:
        pass
    
    @abstractmethod
    def get_service_arn(self) -> str:
        """Return the ARN of the service instance."""
        pass

# Concrete Products
class EC2Service(AWSService):
    def start(self) -> str:
        return "Starting EC2 instance"

    def stop(self) -> str:
        return "Stopping EC2 instance"

    def get_service_arn(self) -> str:
        return "arn:aws:ec2:region:account-id:instance/instance-id"

class RDSService(AWSService):
    def start(self) -> str:
        return "Starting RDS database"

    def stop(self) -> str:
        return "Stopping RDS database"

    def get_service_arn(self) -> str:
        return "arn:aws:rds:region:account-id:db/db-instance-id"

class ECSService(AWSService):
    def start(self) -> str:
        return "Starting ECS cluster"

    def stop(self) -> str:
        return "Stopping ECS cluster"

    def get_service_arn(self) -> str:
        return "arn:aws:ecs:region:account-id:cluster/cluster-name"

# Abstract Factory (AWS Service Creator)
class AWSServiceCreator(ABC):
    @abstractmethod
    def create_service(self) -> AWSService:
        pass

    def manage_service(self, action: str) -> None:
        """
        Factory method to create the service and perform an action
        """
        service = self.create_service()
        
        if action == "start":
            print(service.start())
        elif action == "stop":
            print(service.stop())
        elif action == "arn":
            print(service.get_service_arn())
        else:
            print("Unknown action")

# Concrete Factories
class EC2Creator(AWSServiceCreator):
    def create_service(self) -> AWSService:
        return EC2Service()

class RDSCreator(AWSServiceCreator):
    def create_service(self) -> AWSService:
        return RDSService()

class ECSCreator(AWSServiceCreator):
    def create_service(self) -> AWSService:
        return ECSService()

# Client Code with Dictionary Mapping
def manage_aws_service(service_type: ServiceType, action: str):
    # Mapping of service types to their respective creators
    creator_mapping = {
        ServiceType.EC2: EC2Creator(),
        ServiceType.RDS: RDSCreator(),
        ServiceType.ECS: ECSCreator()
    }

    # Retrieve the correct creator based on the service type
    creator: AWSServiceCreator = creator_mapping.get(service_type)

    if creator:
        creator.manage_service(action)
    else:
        print("Unknown service type")


if __name__ == "__main__":
    manage_aws_service(ServiceType.EC2, "start")
    manage_aws_service(ServiceType.RDS, "stop")
    manage_aws_service(ServiceType.ECS, "arn")
