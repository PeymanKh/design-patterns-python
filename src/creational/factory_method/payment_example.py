"""
Payment Processing System Scenario:
Build a payment processing system for an e-commerce platform that handles different payment methods.

The system should support:
    1. Credit Card payments: Process with card number, CVV, and expiration date
    2. PayPal payments: Process with email and authorization token
    3. Cryptocurrency payments: Process with wallet address and blockchain network

Each notification type should have:
    1. A validate_payment_details() method that checks if payment information is valid (Just print validation steps)
    2. A process_payment(amount: float) method that processes the transaction
    3. A generate_receipt(amount: float) method that returns a formatted receipt string
"""
# Import libraries
from abc import ABC, abstractmethod


## Product & Concrete Products
class PaymentInterface(ABC):
    """Product interface, abstract implementation of payment products"""

    @abstractmethod
    def validate_payment_details(self):
        """Validated payment information"""
        pass

    @abstractmethod
    def process_payment(self, amount: float):
        """Processes the transaction"""
        pass

    @abstractmethod
    def generate_receipt(self, amount: float, status: str):
        """Generates a receipt for the payment"""
        pass


class CreditCardPayment(PaymentInterface):
    """Concrete product for creditcard payment"""
    def __init__(self, card_number: str, cvv: str, expiry: str):
        self.card_number = card_number
        self.cvv = cvv
        self.expiry = expiry

    def validate_payment_details(self):
        print(f"Validating Card ending with {self.card_number[-4:]}")

    def process_payment(self, amount: float):
        print(f"Processing ${amount:,} with card ending with {self.card_number[-4:]}")
        return "Successful"

    def generate_receipt(self, amount: float, status: str):
        print(f"Payment of ${amount:,} with card ending with {self.card_number[-4:]} was {status}")


class PayPalPayment(PaymentInterface):
    """Concrete product for PayPal payment"""
    def __init__(self, email: str, auth_token: str):
        self.email = email
        self.auth_token = auth_token

    def validate_payment_details(self):
        print(f"validating PayPal account with email {self.email}")

    def process_payment(self, amount: float):
        print(f"Processing ${amount:,} with PayPal account {self.email}")
        return "Failed"

    def generate_receipt(self, amount: float, status: str):
        print(f"Payment of ${amount:,} with PayPal account {self.email} was {status}")


class CryptocurrencyPayment(PaymentInterface):
    """Concrete product for Cryptocurrency payment"""
    def __init__(self, wallet_address: str, blockchain_network: str):
        self.wallet_address = wallet_address
        self.blockchain_network = blockchain_network

    def validate_payment_details(self):
        print(f"validating wallet ending with {self.wallet_address[-8:]}")

    def process_payment(self, amount: float):
        print(f"Processing ${amount:,} with wallet ending with {self.wallet_address[-8:]}")
        return "Successful"

    def generate_receipt(self, amount: float, status: str):
        print(f"Payment of ${amount:,} with wallet ending with {self.wallet_address[-8:]} was {status}")



# Creator and Concreate creators
class PaymentCreator(ABC):
    """Factory class for creating processing objects"""

    @abstractmethod
    def create_payment_service(self) -> PaymentInterface:
        """Factory method to return a payment object"""
        pass


    def execute_transaction(self, amount: float):
        """Main business logic to execute the transaction"""
        payment_service = self.create_payment_service()
        payment_service.validate_payment_details()
        process_result = payment_service.process_payment(amount)
        payment_service.generate_receipt(amount, process_result)


class CreditCardPaymentCreator(PaymentCreator):
    """Concrete creator for creditcard payment"""
    def __init__(self, card_number: str, cvv: str, expiry: str):
        self.card_number = card_number
        self.cvv = cvv
        self.expiry = expiry

    def create_payment_service(self) -> PaymentInterface:
        return CreditCardPayment(card_number=self.card_number, cvv=self.cvv, expiry=self.expiry)


class PaypalPaymentCreator(PaymentCreator):
    """Concrete creator for PayPal payment"""

    def __init__(self, email: str, auth_token: str):
        self.email = email
        self.auth_token = auth_token

    def create_payment_service(self) -> PaymentInterface:
        return PayPalPayment(email=self.email, auth_token=self.auth_token)


class CryptocurrencyPaymentCreator(PaymentCreator):
    """Concrete creator for PayPal payment"""

    def __init__(self, wallet_address: str, blockchain_network: str):
        self.wallet_address = wallet_address
        self.blockchain_network = blockchain_network

    def create_payment_service(self) -> PaymentInterface:
        return CryptocurrencyPayment(wallet_address=self.wallet_address, blockchain_network=self.blockchain_network)


if __name__ == "__main__":
    cryptocurrency_payment_processor = CryptocurrencyPaymentCreator(wallet_address="abcdefghigklmnop", blockchain_network="Tron")
    cryptocurrency_payment_processor.execute_transaction(300000.00)
