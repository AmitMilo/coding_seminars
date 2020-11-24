class MyCollection:
    def __init__(self, data, locations):
        self.data = data
        self.locations = locations

    def __iter__(self):
        """
        Generate the iterator for the collection.
        This is the only requirement for a class to be iterable.
        """
        return MyCollection.Iterator(self)

    def __contains__(self, item):
        """
        This method isn't required for a class to be iterable.
        This method is called when we use "x in y".
        For example:
            if 3 in my_collection:
                ...
        """
        # In that case the implementation is simple. We can check if the element is in the decorated data.
        return item in self.data

    class Iterator:
        def __init__(self, my_collection):
            self.my_collection = my_collection
            self.index = 0

        def __iter__(self):
            """
            Most of the functionality of iterator would work without this,
            but returning an iterator for the iterator is a good convention.
            :return: We can simply return the iterator itself.
            """
            return self

        def __next__(self):
            """
            Implement the next step of the iteration.
            After the whole iteration is complete, this method should throw a StopIteration exception.
            (Python syntax handles it and the code doesn't crash).
            """
            if self.index == len(self.my_collection.locations):
                # If iterated over all the locations, the iteration is over.
                raise StopIteration

            # Otherwise, we return the next value in the iteration.
            value = self.my_collection.data[self.my_collection.locations[self.index]]
            self.index += 1
            return value


if __name__ == '__main__':
    data = [1, 2, 3, 4]
    locations = [2, 0, 1, 3]

    my_collection = MyCollection(data, locations)

    # for element in my_collection:
    #     print(element)

    if 5 in my_collection:
        print("Found it!")

