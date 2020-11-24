import numpy as np
import pandas as pd
from abc import ABCMeta, abstractmethod


class MyLoans(metaclass=ABCMeta):
    """
    This is the base abstract method. Defines the behaviour and structure of the subclasses.
    Subclasses differ only in some inner behaviour (the way to extract the interest rate.
    """
    @abstractmethod
    def __init__(self, df):
        self._loan_amnt = df["loan_amnt"]
        self._term = df["term"]

    @abstractmethod
    def get_int_rate(self):
        pass

    def calc_revenue(self):
        return self._loan_amnt * np.power((1 + self.get_int_rate()), self._term) - self._loan_amnt


class MyLCLoans(MyLoans):
    def __init__(self, df):
        super().__init__(df)
        self._int_rate = df["int_rate"]

    def get_int_rate(self):
        return self._int_rate


class MyProsperLoans(MyLoans):
    def __init__(self, df):
        super().__init__(df)
        self._int_rate_str = df["intRate"]

    def get_int_rate(self):
        return self._int_rate_str.astype(np.float64)


def foo(loan: MyLoans):
    print(loan.calc_revenue())
    print(loan.get_int_rate(), end="\n\n")


if __name__ == '__main__':
    common_columns = ["loan_amnt", "term"]
    lc_df = pd.DataFrame([[1000, 12, 0.3], [2500, 36, 0.1]], columns=common_columns + ["int_rate"])
    prosper_df = pd.DataFrame([[1000, 12, "0.3"], [2500, 36, "0.1"]], columns=common_columns + ["intRate"])

    foo(MyLCLoans(lc_df))
    foo(MyProsperLoans(prosper_df))