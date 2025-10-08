"""
Notification System Scenario:
Build a notification system for an application that sends messages through different channels.

The system should support:
    1. Email notifications
    2. SMS notifications
    3. Push notifications

Each notification type should have:
    1. A format_message() Method
    2. A send() Method
"""
# Import libraries
from abc import ABC, abstractmethod


## Product & Concrete Products
class NotificationInterface(ABC):
    """Product Interface, It is an abstract blueprint for creating different notification channels"""
    @abstractmethod
    def format_message(self, message: str) -> str:
        """Format the message to be sent"""
        pass

    @abstractmethod
    def send(self, message: str):
        """Send the message"""
        pass


class EmailNotification(NotificationInterface):
    """Concrete Product, It implements the NotificationInterface for Email Notifications"""
    def format_message(self, message: str) -> str:
        return f"Email notification: {message}"

    def send(self, message: str):
        print(f"Sending email: {message}")


class SMSNotification(NotificationInterface):
    """Concrete Product, It implements the NotificationInterface for SMS Notifications"""
    def format_message(self, message: str) -> str:
        return f"SMS notification: {message}"

    def send(self, message: str):
        print(f"Sending SMS: {message}")


class PushNotification(NotificationInterface):
    """Concrete Product, It implements the NotificationInterface for Push Notifications"""
    def format_message(self, message: str) -> str:
        return f"Push notification: {message}"

    def send(self, message: str):
        print(f"Sending Push: {message}")


## Creator & Concrete Creators
class NotificationCreator(ABC):
    """Factory Class, It creates the notification objects"""

    @abstractmethod
    def create_notification(self) -> NotificationInterface:
        """Factory Method, It creates the notification object based on the channel"""
        pass

    def notify_user(self, message: str):
        """Main business logic, It creates the notification object and sends the message"""
        notification = self.create_notification()
        formatted_message = notification.format_message(message)
        notification.send(formatted_message)


class EmailNotificationCreator(NotificationCreator):
    """Concrete Factory, It creates the EmailNotification object"""
    def create_notification(self) -> NotificationInterface:
        return EmailNotification()


class SMSNotificationCreator(NotificationCreator):
    """Concrete Factory, It creates the SMSNotification object"""
    def create_notification(self) -> NotificationInterface:
        return SMSNotification()


class PushNotificationCreator(NotificationCreator):
    """Concrete Factory, It creates the PushNotification object"""
    def create_notification(self) -> NotificationInterface:
        return PushNotification()



if __name__ == "__main__":
    email_creator = EmailNotificationCreator()
    email_creator.notify_user("Hello, this is an email notification")

    sms_creator = SMSNotificationCreator()
    sms_creator.notify_user("Hello, this is an SMS notification")