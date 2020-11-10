DOG_DEFAULT_LEGS = 4


class Dog:
    def __init__(self, name, legs=None):
        """
        This is the constructor method.
        Here we create the instance's initial state.
        :param name: the name given to the dog by its owners.
        """
        self.name = name
        self.legs = legs or DOG_DEFAULT_LEGS

    def bark(self):
        """
        This method defines dog behaviour of barking
        """
        print(f"Woof! My name is {self.name}.")

    def __str__(self):
        """
        This method defines the string representation of the object.
        :return:
        """
        return f"""Dog:
        Name: {self.name}
        Number of legs: {self.legs}"""

    def __eq__(self, other):
        """
        This method defines the way to compare a dog object to another object (ANY OBJECT!)
        """
        return self.name == other.name and self.legs == other.legs

    def __add__(self, other):
        """
        Defines the wat to add a dog object to another (any) object.
        Defines the behaviour for self + other.
        """
        new_name = " ".join([self.name, other.name])
        new_legs = (self.legs + other.legs) // 2

        return Dog(new_name, new_legs)

    def __radd__(self, dog_name):
        """
        Same as above, but defines behaviour for other + self.
        Notice: when using customized classes, __add__ is preceded by the interpreter over __radd__.
        Thus: Foo() + Goo() invokes Foo().__add__(Goo())
        """

        return self + other   # Same as calling self.__add__(other)


if __name__ == '__main__':
    first_dog = Dog("Bolt")
    second_dog = Dog("Bolt", 4)
    third_dog = Dog("Spicy", 3)

    print(first_dog, end="\n\n")
    print(first_dog == second_dog)
    print(second_dog == third_dog, end="\n\n")

    new_dog = first_dog + third_dog
    print(new_dog)
