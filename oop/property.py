class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Foo:
    def __init__(self):
        self.__secret = 5
        self.__big_val = None
        self.__x = 3
        self.__y = 7

    @property
    def secret(self):
        """
        In this case, we allow anyone to read the property.
        """
        return self.__secret

    @secret.setter
    def secret(self, value):
        """
        We control the assignment operator of the property.
        We allow only positive values.
        """
        if value > 0:
            self.__secret = value
        else:
            print("Please insert positive value.")

    # @secret.deleter
    # def secret(self):
    #     pass

    # As we don't define secret deleter, secret is not delete-able.

    @property
    def big_val(self):
        """
        Here we have a member (the big value shouldn't be calculated more than once).
        However, this calculation is long and we want to avoid it if possible (lazy calculation).
        """
        if not self.__big_val:
            val = 0
            for i in range(1000):
                val += i

            self.__big_val = val
        return self.__big_val

    @property
    def point(self):
        """
        We want to hide our implementation from the user (while we ensure ha gets the interface he needs).
        That way, we can give the property a name different from the member name and use our own implementation to
        store the data.
        """
        return Point(self.__x, self.__y)

    @point.setter
    def point(self, point: Point):
        self.__x = point.x
        self.__y = point.y


if __name__ == '__main__':
    foo = Foo()
    print(foo.secret)
    foo.secret = -5
    foo.secret = 100
    print(foo.secret)

    print(type(foo.point))

    print(foo.big_val)