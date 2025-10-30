# Import libraries
from abc import ABC, abstractmethod
from random import randrange


class EventManager(ABC):
    """
    The subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, subscriber):
        """Attach a subscriber to the subject."""
        pass

    @abstractmethod
    def detach(self, subscriber):
        """Detach a subscriber from the subject."""
        pass

    @abstractmethod
    def notify(self):
        """Notify all subscribers about an event."""
        pass


class ConcreteEventManager(EventManager):
    """
    The EventManager owns some important state and notifies observers when the state changes.
    """
    def __init__(self):
        self._subscribers = []
        self._state = None

    def attach(self, observer):
        print("Event Manager: Attached a subscriber.")
        self._subscribers.append(observer)

    def detach(self, observer):
        print("Event Manager: Detached a subscriber.")
        if observer in self._subscribers:
            self._subscribers.remove(observer)

    def notify(self):
        print("Event Manager: Notifying observers...")
        for subscriber in self._subscribers:
            subscriber.update(self)

    def business_logic(self):
        print("\nEvent Manager: I'm changing my state.")
        self._state = randrange(0, 10)
        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()



class Subscriber(ABC):
    """
    The Subscriber interface declares the update method, used by subjects.
    """
    @abstractmethod
    def update(self, subject: EventManager) -> None:
        """Receive update from the EventManager"""
        pass


class ConcreteObserverA(Subscriber):
    def update(self, subject: EventManager) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Subscriber):
    def update(self, subject: EventManager) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")



if __name__ == "__main__":
    # The client code.

    event_manager = ConcreteEventManager()

    observer_a = ConcreteObserverA()
    event_manager.attach(observer_a)

    observer_b = ConcreteObserverB()
    event_manager.attach(observer_b)

    event_manager.business_logic()
    event_manager.business_logic()

    event_manager.detach(observer_a)

    event_manager.business_logic()

