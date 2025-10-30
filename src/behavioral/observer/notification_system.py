"""
Scenario: Notification System for Online Learning Platform

You’re building a simple notification system for an online learning platform.

There are multiple types of users:
    - Students
    - Instructors

When a new course assignment is posted, several types of notifications may go out:
    - Students get a notification about the new assignment for their course.
    - Instructors get a notification summarizing all assignments added to their courses.
"""
# Import libraries
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

from src.behavioral.observer.template import Subscriber



class NotificationManager(ABC):
    """Subject Interface. It manages subscribers"""

    @abstractmethod
    def attach(self, subscriber: Subscriber):
        """Attach a new subscriber"""
        pass

    @abstractmethod
    def detach(self, subscriber: Subscriber):
        """Detach an existing subscriber"""
        pass

    @abstractmethod
    def notify(self):
        """Notify all subscribers about an event"""
        pass


class ConcreteNotificationManager(NotificationManager):
    """Concrete Subject. It manages subscribers"""
    def __init__(self):
        self._subscribers: List[Subscriber] = []

    def attach(self, subscriber: Subscriber):
        print("Notification Manager: Attached a subscriber.")
        self._subscribers.append(subscriber)

    def detach(self, subscriber: Subscriber):
        print("Notification Manager: Detached a subscriber.")
        if subscriber in self._subscribers:
            self._subscribers.remove(subscriber)

    def notify(self):
        print("Notification Manager: Notifying observers...")
        for subscriber in self._subscribers:
            subscriber.update(self)


class Subscriber(ABC):
    """Abstract Subscriber Interface"""
    @abstractmethod
    def update(self, subject: NotificationManager):
        """Update state and notify"""
        pass


class StudentSubscriber(Subscriber):
    """Concrete Subscriber. It notifies students about new assignments"""
    def update(self, subject: NotificationManager):
        print("Message send to StudentSubscriber: {You have a new assignment!}")


class InstructorSubscriber(Subscriber):
    """Concrete Subscriber. It notifies instructors about new assignments"""
    def update(self, subject: NotificationManager):
        print("Message send to InstructorSubscriber: {A new assignment has been posted!}")


if __name__ == "__main__":
    notification_manager = ConcreteNotificationManager()
    notification_manager.attach(StudentSubscriber())
    notification_manager.attach(InstructorSubscriber())
    notification_manager.notify()