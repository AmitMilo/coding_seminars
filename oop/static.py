class MyMath:
    PI = 3.14  # PI is constant and equal for all members of MyMath. However,
    # this value is connected to the MyMath class and thus is put as a member (constant) of the class.

    def __init__(self, x):
        self.x = x

    def foo(self):
        """
        This is an instance method. It depends on the instance inner state.
        """
        print(self.x)

    @staticmethod
    def pow(x, y):
        """
        Power method is constant at my math, and doesn't depend on object's inner state.
        As it is connected to the class, we put it as static method.
        """
        return pow(x, y)

    @classmethod
    def create_double(cls, x):
        """
        This method doesn't depend on a specific instance (in fact, it creates an instance.
        However, it depends on the class it is executed from (MyMath class or one of its subclasses).
        """
        return cls(x * 2)


class MyMath2(MyMath):
    def __init__(self, x):
        super().__init__(x)
        self.y = x + 1


    def foo(self):
        """
        This is an instance method. It depends on the instance inner state.
        """
        print(self.x)
        print(self.y)


if __name__ == '__main__':
    # my_math = MyMath(10)
    # my_math.foo()
    #
    # print(MyMath.PI)   # But we can use my_math.PI!
    # print(my_math.pow(5, 3))   # Or MyMath.pow(5, 3)

    my_math1 = MyMath.create_double(10)   # We can even use here my_math.create_double.
    my_math2 = MyMath2.create_double(10)   # We can even use here my_math.create_double.
    # However, it somewhat counter-intuitive.

    # my_math1.foo()
    # my_math2.foo()
    print(type(my_math1))
    print(type(my_math2))
