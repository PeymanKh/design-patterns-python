# Observer
Observer is a behavioral design pattern that lets you define a subscription mechanism to notify multiple objects
about any events that happen to the object they're observing. We define a subject (observable) to maintain a list 
of its dependents (observers) and automatically notify them about any state changes.

# Components
- **Subject:** Keep track of observers and updates them when state changes.
- **Observer:** Defines the interface for objects that should be notified of changes in a subject.
- **Attach/Detach:** Methods that allow observers to subscribe or unsubscribe from the observable.
- **Notify:** Method that notifies all observers about a state change.

