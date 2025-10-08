# Abstract Factory
Abstract factory is a creational pattern that lets you produce families of related 
objects without specifying their concrete classes. It's often called a "factory of 
factories" because it creates other factories.

## Components
1. **Abstract Product:** Interfaces defining what each product type should look like 
2. **Concrete Products:** Actual implementations of abstract products for specific families
3. **Abstract Factory:** Interface declaring creation methods for all products in the family
4. **Concrete Factories:** Classes implementing the abstract factory to create specific product families
5. **Client:** Uses factories and products through abstract interfaces only—never knows about concrete classes

# Applications
1. Your code needs to create sets of related objects that work together, but at the time of writing the code, you either:
    - Don't know exactly which families will be needed 
    - Want to easily add new families in the future without changing existing code
2. The factory gives you methods to create all products in a family (create_compute(), create_storage(), create_database()). When you use these methods, you're guaranteed all products come from the same family.



