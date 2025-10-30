# Strategy
Strategy is a behavioral design pattern that lets you design a family of algorithms, put each of them into a separate 
class, and make their objects interchangeable. In simple words, it enables objects to select and switch between
different algorithms at runtime.


## Components
1. **Context:** The main object that holds the reference to a strategy object.
2. **Strategy Interface:** An interface that defines the algorithm.
3. **Concrete Strategies:** Specific concrete implementations of the strategy interface.
4. **Client:** Responsible for selecting the appropriate strategy and providing it to the context.
