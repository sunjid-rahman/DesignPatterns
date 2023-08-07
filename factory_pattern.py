class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

    @classmethod
    def create(cls, animal_type, name):
        if animal_type == "Dog":
            return Dog(name)
        elif animal_type == "Cat":
            return Cat(name)
        else:
            raise ValueError(f"Invalid animal type: {animal_type}")


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


if __name__ == '__main__':
    dog = Animal.create("Dog", "Fido")
    print(dog.speak())  # Output: "Woof"

    cat = Animal.create("Cat", "Whiskers")
    print(cat.speak())  # Output: "Meow"

