import copy


class Prototype:
    def __init__(self):
        self.objects = {}

    def register(self, name, obj):
        self.objects[name] = obj

    def unregister(self, name):
        del self.objects[name]

    def clone(self, obj_name, **kwargs):
        obj = copy.deepcopy(self.objects.get(obj_name))
        obj.__dict__.update(kwargs)
        return obj


class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age}, gender='{self.gender}')"


if __name__ == '__main__':
    prototype = Prototype()

    person1 = Person("John", 30, "Male")
    prototype.register("person1", person1)

    person2 = prototype.clone("person1", name="Jane", age=25)
    print(person1) # Output: Person(name='John', age=30, gender='Male')
    print(person2) # Output: Person(name='Jane', age=25, gender='Male')
