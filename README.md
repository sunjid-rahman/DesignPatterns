# Details

Creational Patterns: These patterns are focused on object creation mechanisms, and they help to create objects in a manner that is suitable for the situation. Some examples of creational patterns include:


Singleton Pattern: ensures that only one instance of a class is created and provides a global point of access to it.

Factory Pattern: provides an interface for creating objects, but allows subclasses to decide which classes to instantiate.

Builder Pattern: separates the construction of a complex object from its representation, allowing the same construction process to create different representations.

Prototype Pattern: creates new objects by cloning existing ones, without coupling the code to the actual classes of the objects.


Structural Patterns: These patterns are concerned with object composition and they focus on how objects are connected or related to each other. Some examples of structural patterns include:


Adapter Pattern: converts the interface of a class into another interface that clients expect, allowing classes to work together despite incompatible interfaces.

Bridge Pattern: separates an object's interface from its implementation, allowing the two to vary independently.

Composite Pattern: treats a group of objects as a single object, allowing the same operations to be performed on the group and on individual objects.

Decorator Pattern: adds functionality to an object dynamically, without changing its original structure.


Behavioral Patterns: These patterns deal with communication between objects, defining how objects communicate and interact with each other. Some examples of behavioral patterns include:

Command Pattern: encapsulates a request as an object, allowing the parameterization of clients with different requests, queues, or logs, and supporting undoable operations.

Observer Pattern: defines a one-to-many dependency between objects, so that when one object changes state, all its dependents are notified and updated automatically.

Strategy Pattern: defines a family of algorithms, encapsulates each one, and makes them interchangeable, allowing the algorithm to vary independently from clients that use it.

Template Method Pattern: defines the skeleton of an algorithm in a superclass, allowing its subclasses to redefine certain steps of the algorithm without changing its structure.


# Creational Design Patterns


1. Singleton Pattern:

The Singleton Pattern is a creational design pattern that ensures that a class has only one instance and provides a global point of access to that instance. The singleton pattern is useful when we need to ensure that there is only one instance of a class in the entire system, such as in a database connection or configuration object.

In Python, the singleton pattern can be implemented using a class with a private constructor and a static instance variable. Here's an example of how to implement the singleton pattern in Python:


```
class Singleton:
    __instance = None   # private variable to hold the instance
    
    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("Singleton class cannot be instantiated more than once")
        else:
            Singleton.__instance = self
            self.value = "This is a singleton instance."

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance


if __name__ == "__main__":
    s1 = Singleton.getInstance()
    s2 = Singleton.getInstance()
    print(s1 == s2) # Output: True
    print(s1.value) # Output: This is a singleton instance.```
```

 In this example, we have a Singleton class with a private constructor that can only be called from within the class. The class also has a static instance variable _instance that holds the single instance of the class. The __new__ method of the class checks whether the instance variable is None, and if so, creates a new instance of the class and assigns it to the _instance variable. If the instance variable is not None, it returns the existing instance.

To create an instance of the Singleton class, we simply call the class constructor as usual. Since the constructor is private, we can only create an instance from within the class, but the singleton pattern ensures that we only get the one instance of the class. We can create multiple instances of the class, but they will all be the same instance.

This implementation of the singleton pattern ensures that there is only one instance of the Singleton class in the system, regardless of how many times the class is instantiated. It also provides a global point of access to that instance, allowing us to easily access the singleton instance from anywhere in the system.


2. Factory Pattern

The Factory Pattern is a creational design pattern that provides an interface for creating objects without specifying the exact class to create. The factory method pattern defines an interface for creating an object, but lets subclasses decide which class to instantiate.

In Python, the factory pattern can be implemented using a class method or a separate factory class. Here's an example of how to implement the factory pattern in Python using a class method:

----code----

In this example, we have an Animal class with a create class method that takes an animal_type argument and returns an instance of the appropriate subclass (Dog or Cat). The Dog and Cat subclasses implement the speak method to return the animal's sound.

To create an instance of an animal, we call the create method on the Animal class with the appropriate animal type and name. The create method then returns an instance of the appropriate subclass.

This implementation of the factory pattern allows us to create instances of Dog and Cat without having to know the exact class to create. It also makes it easy to add new animal types in the future by simply creating a new subclass and updating the create method to handle it.


3. Builder Pattern

The Builder Pattern is a creational design pattern that separates the construction of a complex object from its representation, allowing the same construction process to create different representations. The builder pattern is useful when the construction of an object requires several steps that may vary based on certain conditions.

In Python, the builder pattern can be implemented using a builder class that handles the construction of the object step by step. Here's an example of how to implement the builder pattern in Python:

----code----

In this example, we have a Person class that has name, age, and gender attributes. We also have a PersonBuilder class that handles the construction of the Person object. The PersonBuilder class has methods for setting the name, age, and gender attributes of the Person object. The build method returns the Person object after it has been constructed.

To create a Person object, we create a PersonBuilder object and use its methods to set the attributes of the Person object. We then call the build method to construct the Person object and return it.

This implementation of the builder pattern allows us to create Person objects with different attributes without having to create separate constructors for each combination of attributes. It also allows us to add or remove steps in the construction process without affecting the other steps.

4. Prototype Pattern

The Prototype Pattern is a creational design pattern that allows us to create new objects by copying or cloning existing objects. The prototype pattern is useful when creating new objects from scratch is expensive or complex, and we can save time and resources by copying existing objects instead.

In Python, the prototype pattern can be implemented using a prototype object and a clone method. Here's an example of how to implement the prototype pattern in Python:

----code----

In this example, we have a Prototype class that stores a dictionary of objects and provides methods for registering, unregistering, and cloning those objects. We also have a Person class that has name, age, and gender attributes.

To use the prototype pattern, we create a Prototype object and register an object with it. We can then clone the object and modify its attributes as needed. The clone method of the Prototype class uses the deepcopy function from the copy module to create a new copy of the object and then updates its attributes with any keyword arguments provided.

To create a new Person object, we first create an existing Person object person1 and register it with the Prototype object. We can then clone the person1 object and modify its attributes to create a new Person object person2.

This implementation of the prototype pattern allows us to create new objects by copying existing objects, which can save time and resources compared to creating new objects from scratch. It also allows us to easily modify the attributes of the new objects by passing keyword arguments to the clone method.

# Structural Patterns

1. Adapter Pattern

The Adapter Pattern is a structural design pattern that allows objects with incompatible interfaces to work together by creating an adapter object that translates the interface of one object into the interface expected by another object. This pattern is useful when you have existing code or components that cannot be easily modified to work with other components, but you still need them to work together.

In Python, the Adapter Pattern can be implemented using a class that acts as an adapter between two incompatible interfaces. The adapter class implements the interface of one object and translates the requests into a format that the other object can understand. Here's an example of how to implement the Adapter Pattern in Python:

----code ----

The code defines two classes for temperature representation, CelsiusTemperature and FahrenheitTemperature, which have different methods for getting the temperature in Celsius and Fahrenheit, respectively.

Then, it defines an interface TemperatureAdapter that specifies a common method for getting the temperature, which will be implemented by the adapter classes.

The code defines two adapter classes, CelsiusToFahrenheitAdapter and FahrenheitToCelsiusAdapter, which implement the TemperatureAdapter interface and convert temperatures between Celsius and Fahrenheit.

Finally, the client code creates instances of the temperature classes and the adapter classes and uses them to convert temperatures and print the results. The first line prints the temperature in Fahrenheit corresponding to 20 degrees Celsius, and the second line prints the temperature in Celsius corresponding to 68 degrees Fahrenheit.

2. Bridge Pattern

The Bridge pattern is a structural design pattern that separates an abstraction from its implementation so that they can vary independently. In Python, we can implement the Bridge pattern using classes and inheritance.

Here is an example implementation of the Bridge pattern in Python:

----code----

In this example, we have an abstraction Shape with two concrete implementations Circle and Square. We also have an implementation hierarchy with two concrete implementations VectorRenderer and RasterRenderer. The Shape class has a reference to an implementation of Renderer class. The draw method of the Shape class calls the render method of the implementation of Renderer class to draw the shape.

The client code creates instances of Circle and Square, sets their color, and renders them using the VectorRenderer and RasterRenderer implementations.









