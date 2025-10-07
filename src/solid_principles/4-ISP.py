"""
4. Interface Segregation Principle:
Don't create fat interfaces that force classes to implement methods they don't need.
Instead, create lean, focused interfaces tailored to specific client needs.
"""

# BAD Design
from abc import ABC, abstractmethod


class Worker(ABC):
    """Fat interface - forces all workers to implement all methods!"""

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class HumanWorker(Worker):
    """Humans do all three - fine"""

    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

    def sleep(self):
        print("Human sleeping")


class RobotWorker(Worker):
    """Robot doesn't eat or sleep - forced to implement useless methods!"""

    def work(self):
        print("Robot working")

    def eat(self):
        # Robots don't eat! But forced to implement this
        raise NotImplementedError("Robots don't eat!")

    def sleep(self):
        # Robots don't sleep! But forced to implement this
        raise NotImplementedError("Robots don't sleep!")



## GOOD DESIGN
from abc import ABC, abstractmethod


# Split into smaller, focused interfaces
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class Sleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass


# Now classes only implement what they need
class HumanWorker(Workable, Eatable, Sleepable):
    """Humans implement all three interfaces"""

    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

    def sleep(self):
        print("Human sleeping")


class RobotWorker(Workable):
    """Robots only implement Workable - no forced methods!"""

    def work(self):
        print("Robot working 24/7")


# Usage - both work perfectly
def manage_worker(worker: Workable):
    worker.work()


manage_worker(HumanWorker())  # ✓
manage_worker(RobotWorker())  # ✓
