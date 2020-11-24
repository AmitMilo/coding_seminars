def assert_no_none(func):
    """
    A decorator used to assert all the arguments inserted to a method are not None.
    Raise an assertion error if there are any Nones.
    :param func: This the original function we wrap.
    :return: A wrapping method, which validates there aren't any Nones in the arguments.
    """

    def wrapper(*args, **kwargs):
        """
        This is the wrapping method to replace the original one.
        In our case, the wrapper method validating there are no Nones in the arguments, and then calls the original
        function with the original parameters.
        :param args: The arguments of the original function are passed into here, as this replaces the original function.
        :param kwargs: Kwargs are also passed in here.
        :return: After adding the meta behavior, the wrapper is expected to return a call to the original function.
        """
        args_are_not_none = (element is not None for element in args)
        kwargs_are_not_none = (element is not None for element in kwargs.values())

        assert all(args_are_not_none)
        assert all(kwargs_are_not_none)

        return func(*args, **kwargs)

    return wrapper


@assert_no_none
def foo(x, y, z):
    print(x + y + z)


def goo(x):
    print(x)


goo = assert_no_none(goo)

if __name__ == '__main__':
    # foo(1, 2, z=3)
    # foo(None, 2, z=3)
    # foo(1, 2, z=None)

    # goo(1)
    # goo(x=1)
    goo(None)
    # goo(x=None)
