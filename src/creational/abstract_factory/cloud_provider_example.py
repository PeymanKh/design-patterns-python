"""
Cloud Service Provider Scenario:
Build a cloud infrastructure management system that deploys applications across different cloud providers.

System should support:
    1. AWS (Amazon Web Services)
    2. Azure (Microsoft)
    3. GCP (Google Cloud Platform)

Infrastructure Components (Products in Each Family)
Each cloud provider needs these services:
    1. Compute Instance: Has a launch() method that prints instance details (e.g., "Launching AWS EC2 instance..." or "Launching Azure VM...")
    2. Storage Service: Has a create_bucket() method that prints storage creation (e.g., "Creating AWS S3 bucket..." or "Creating Azure Blob Storage...")
    3. Database Service: Has a provision() method that prints database setup (e.g., "Provisioning AWS RDS..." or "Provisioning Azure SQL Database...")
"""
# Import libraries
from abc import ABC, abstractmethod



########################## Abstract Products ##########################
class ComputingInstance(ABC):
    """Abstract computing instance interface which acts as a blueprint for concrete products"""
    @abstractmethod
    def launch(self):
        """Lunches a computing instance to cloud provider"""
        pass

class StorageService(ABC):
    """Abstract storage service interface which acts as a blueprint for concrete products"""
    @abstractmethod
    def create_bucket(self):
        """Initializes a new bucket in the cloud provider"""
        pass

class DatabaseService(ABC):
    """Abstract database service interface which acts as a blueprint for concrete products"""
    @abstractmethod
    def provision(self):
        """Makes the database ready to use in the cloud provider"""
        pass


########################## Concrete Products ##########################
class AWSComputingInstance(ComputingInstance):
    """Concrete computing instance for AWS"""
    def launch(self):
        print("Launching AWS EC2 instance...")

class AWSStorageService(StorageService):
    """Concrete storage service for AWS"""
    def create_bucket(self):
        print("Creating AWS S3 bucket...")

class AWSDatabaseService(DatabaseService):
    """Concrete database service for AWS"""
    def provision(self):
        print("Provisioning AWS RDS...")


class AzureComputingInstance(ComputingInstance):
    """Concrete computing instance for Azure"""
    def launch(self):
        print("Launching Azure VM...")

class AzureStorageService(StorageService):
    """Concrete storage service for Azure"""
    def create_bucket(self):
        print("Creating Azure Blob Storage...")

class AzureDatabaseService(DatabaseService):
    """Concrete database service for Azure"""
    def provision(self):
        print("Provisioning Azure SQL Database...")


class GCPComputingInstance(ComputingInstance):
    """Concrete computing instance for GCP"""
    def launch(self):
        print("Launching GCP Compute Engine...")

class GCPStorageService(StorageService):
    """Concrete storage service for GCP"""
    def create_bucket(self):
        print("Creating GCP Cloud Storage...")

class GCPDatabaseService(DatabaseService):
    """Concrete database service for GCP"""
    def provision(self):
        print("Provisioning GCP Spanner...")


########################## Abstract Factory ##########################
class CloudServiceCreator(ABC):
    """Abstract factory interface for creating cloud services"""

    @abstractmethod
    def create_compute_instance(self):
        pass

    @abstractmethod
    def create_storage_service(self):
        pass

    @abstractmethod
    def create_database_service(self):
        pass


########################## Concrete Factory ##########################
class AWSCloudServiceCreator(CloudServiceCreator):
    """Concrete factory for creating AWS objects"""
    def create_compute_instance(self) -> ComputingInstance:
        return AWSComputingInstance()

    def create_storage_service(self) -> StorageService:
        return AWSStorageService()

    def create_database_service(self) -> DatabaseService:
        return AWSDatabaseService()


class AzureCloudServiceCreator(CloudServiceCreator):
    """Concrete factory for creating Azure objects"""

    def create_compute_instance(self) -> ComputingInstance:
        return AzureComputingInstance()

    def create_storage_service(self) -> StorageService:
        return AzureStorageService()

    def create_database_service(self) -> DatabaseService:
        return AzureDatabaseService()


class GCPCloudServiceCreator(CloudServiceCreator):
    """Concrete factory for creating GCP objects"""

    def create_compute_instance(self) -> ComputingInstance:
        return GCPComputingInstance()

    def create_storage_service(self) -> StorageService:
        return GCPStorageService()

    def create_database_service(self) -> DatabaseService:
        return GCPDatabaseService()


########################## Client ##########################
class Client:
    def __init__(self, provider: CloudServiceCreator):
        self.provider = provider

    def deploy_application(self):
        compute_instance = self.provider.create_compute_instance()
        storage_service = self.provider.create_storage_service()
        database_service = self.provider.create_database_service()

        compute_instance.launch()
        storage_service.create_bucket()
        database_service.provision()


if __name__ == "__main__":
    client = Client(provider=AWSCloudServiceCreator())
    client.deploy_application()