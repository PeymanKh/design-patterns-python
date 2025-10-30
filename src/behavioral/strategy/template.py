# Import libraries
from abc import ABC, abstractmethod
from typing import List


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """
    @abstractmethod
    def calculate(self, data: List) -> List:
        pass


class ConcreteStrategyA(Strategy):
    def calculate(self, data: List) -> List:
        return sorted(data)


class ConcreteStrategyB(Strategy):
    def calculate(self, data: List) -> List:
        return reversed(sorted(data))


class Context:
    """
    The Context defines the interface of interest to clients.
    """
    def __init__(self, strategy: Strategy) -> None:
        """
        Usually, the Context accepts a strategy through the constructor, but
        also provides a setter to change it at runtime.
        """
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def execute_strategy(self, data: List) -> List:
        return self._strategy.calculate(data)



if __name__ == "__main__":
    # The client code picks a concrete strategy and passes it to the context.
    # The client should be aware of the differences between strategies in order
    # to make the right choice.

    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    result1 = context.execute_strategy([3, 2, 24, 1])
    print(result1)

    print("Client: Strategy is set to reverse sorting.")
    result2= context.strategy = ConcreteStrategyB()
    print(result2)