from oop.basic_dog_class import Dog


class Pomeranian(Dog):
    def __init__(self, name):
        super().__init__(name)
        print("Pomeranian was created.", end="\n\n")

    def bark(self):
        #super().bark()
        print("I'm costly.")


if __name__ == '__main__':
    my_dog = Pomeranian("Bolt")
    my_dog.bark()
    print(my_dog.legs)
    print(my_dog.favorite_color(), end="\n\n")

    print(isinstance(my_dog, Pomeranian))
    print(isinstance(my_dog, Dog))