# Factory Method
Factory method is a creational design pattern that provides an interface for creating objects in a superclass 
but allows subclasses to alter the type of objects that will be created.

In simple words, this pattern separates the code that creates an object from the code that runs it. Therefore, it is easier to extend the project because we do not need
to change how the objects are used, only we add a new creator subclass.

## Components:
1. **Product:** Defines the common interface that all `Concrete Products` must implement. Returns nothing, it is just an abstract method.
2. **Concrete Product:** Actual implementation of the `Product` interface; the real objects the factory creates. Returns specific data or behavior through methods defined by the `Product` interface.
3. **Creator (Factory):** Declares the abstract factory method that subclasses will override; may contain common logic that uses products. The factory method itself returns a `Product object`.
4. **Concrete Creator:** Implements the factory method to instantiate and return a specific `Concrete Product`.

## Applications:
1. Use when your code needs to create objects, but at the time of writing you do not know exactly which specific types of objects will be needed when the program runs in the future.
2. You're building a library/framework that other developers will use, and you want to let them customize how certain objects are created without rewriting your code.