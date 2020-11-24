import time


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Foo:
    def __init__(self):
        self._secret = 5
        self._big_val = None
        self._x = 3
        self._y = 7

    @property
    def secret(self):
        """
        In this case, we allow anyone to read the property.
        """
        return self._secret

    @secret.setter
    def secret(self, value):
        """
        We control the assignment operator of the property.
        We allow only positive values.
        """
        if value > 0:
            self._secret = value
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
        if not self._big_val:
            val = 0
            for i in range(20000000):
                val += i

            self._big_val = val
        return self._big_val

    @property
    def point(self):
        """
        We want to hide our implementation from the user (while we ensure ha gets the interface he needs).
        That way, we can give the property a name different from the member name and use our own implementation to
        store the data.
        """
        return Point(self._x, self._y)

    @point.setter
    def point(self, point: Point):
        self._x = point.x
        self._y = point.y


if __name__ == '__main__':
    foo = Foo()
    # print(foo.secret)
    # #foo.secret = -5
    # foo.secret = 100
    # print(foo.secret)


    foo.big_val = 3
    # print(type(foo.point))
    # #
    # print(foo._big_val)
    #
    # start = time.time()
    # print(foo.big_val)
    #
    # print(f"Duration: {time.time() - start}")
    # print(foo._big_val)
    #
    # start = time.time()
    # print(foo.big_val)
    #
    # print(f"Duration: {time.time() - start}")