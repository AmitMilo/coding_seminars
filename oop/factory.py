from abc import ABCMeta, abstractmethod
from typing import List


class Sorter(metaclass=ABCMeta):
    def __init__(self):
        self._list = list()

    def add_string(self, string):
        self._list.append(string)

    @abstractmethod
    def sort(self) -> List[str]:
        pass


class FirstLetterSorter(Sorter):
    def sort(self) -> List[str]:
        return sorted(self._list, key=lambda string: string[0])


class LastLetterSorter(Sorter):
    def sort(self) -> List[str]:
        return sorted(self._list, key=lambda string: string[-1])


class ZFirstSorter(Sorter):
    def sort(self) -> List[str]:
        start_with_z = list()
        others = list()
        for item in self._list:
            if item[0].lower() == "z":
                start_with_z.append(item)
            else:
                others.append(item)

        return sorted(start_with_z) + sorted(others)


class SorterFactory:
    @staticmethod
    def get_sorter(sorter_type):
        if sorter_type == "first_letter":
            return FirstLetterSorter()
        elif sorter_type == "last_letter":
            return LastLetterSorter()
        elif sorter_type == "z_first":
            return ZFirstSorter()


if __name__ == '__main__':
    sorter_type = input("Enter sorter type: ")

    sorter = SorterFactory.get_sorter(sorter_type)
    sorter.add_string("Hello")
    sorter.add_string("Zebra")
    sorter.add_string("Zoo")
    sorter.add_string("All")
    sorter.add_string("Drum")
    sorter.add_string("Banana")

    print(sorter.sort())