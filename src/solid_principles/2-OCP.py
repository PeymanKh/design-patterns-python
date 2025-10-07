"""
2. Open-Closed Principle:
Software entities should be open for extension but closed for modification.
In simple words, we should be able to add new features without modifying the existing code!
"""

## BAD DESIGN
class NotificationService:

    def send_notification(self, message: str, channel: str):
        if channel == "email":
            # Send email
            print(f"Sending email: {message}")
        elif channel == "telegram":
            # Send Telegram message
            print(f"Sending Telegram: {message}")
        elif channel == "slack":
            # Send Slack message
            print(f"Sending Slack: {message}")


## GOOD DESIGN
from abc import ABC, abstractmethod


# Closed for modification
class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message: str):
        pass


# Open for extension - add new channels without modifying existing code
class EmailNotification(NotificationChannel):
    def send(self, message: str):
        print(f"Sending email: {message}")


class TelegramNotification(NotificationChannel):
    def send(self, message: str):
        print(f"Sending Telegram: {message}")


class SlackNotification(NotificationChannel):
    def send(self, message: str):
        print(f"Sending Slack: {message}")


# Add Discord later - NO modification to existing code!
class DiscordNotification(NotificationChannel):
    def send(self, message: str):
        print(f"Sending Discord: {message}")


# The service is closed for modification
class NotificationService:
    def __init__(self, channels: list[NotificationChannel]):
        self.channels = channels

    def notify(self, message: str):
        for channel in self.channels:
            channel.send(message)
