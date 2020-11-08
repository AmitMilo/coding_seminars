DOG_DEFAULT_LEGS = 4


class Dog:
    def __init__(self, name):
        """
        This is the constructor method.
        Here we create the instance's initial state.
        :param name: the name given to the dog by its owners.
        """
        self.name = name
        self.legs = DOG_DEFAULT_LEGS
        self.__private_data = "foo"
        self._semi_private = "goo"
        print("Dog was created.")

    def bark(self):
        """
        This method defines dog behaviour of barking
        """
        print(f"Woof! My name is {self.name}.")

    def favorite_color(self):
        """
        Another behaviour of the dog. Now returning a value.
        Notice we could replace it with a member and initialize it the constructor.
        We can even do better with the property decorator.
        """
        if self.legs & 1:
            return "Blue"  # Odd dogs are Democrats
        return "Red"


if __name__ == '__main__':
    my_dog = Dog("Bolt")
    my_dog.bark()
    print(my_dog.legs)
    print(my_dog.favorite_color())

    # print(my_dog._semi_private)
    # print(my_dog.__private_data)
