from abc import ABCMeta, abstractmethod


class Ball(metaclass=ABCMeta):
    def __init__(self, size):
        """
        Even though we don't initialize abstract classes, it still may have a constructor be called from the children's
        constructor.
        :param size: The size of the ball (member that may be shared among balls).
        """
        self.size = size

        # Set initial location
        self.x = 0

    def throw(self):
        self.x += 5

    @abstractmethod
    def describe(self):
        """
        We may require children classes to implement some methods.
        :return:
        """
        pass

    def describe_and_say_hi(self):
        """
        We still may call abstract method.
        """
        self.describe()
        print("hi")


class SoccerBall(Ball):
    def describe(self):
        print(f"I'm a soccer ball. My size is {self.size}. My location is {self.x}")


class BasketBall(Ball):
    def describe(self):
        print(f"I'm a basketball ball, my size is {self.size}. My location is {self.x}.")


if __name__ == '__main__':
    soccer = SoccerBall(5)
    basket = BasketBall(10)

    soccer.describe()

    basket.throw()
    basket.describe_and_say_hi()

    # ball = Ball(7)