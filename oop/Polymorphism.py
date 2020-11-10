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
        self.loan_amnt = df["loan_amnt"]
        self.term = df["term"]
        self.int_rate = None   # Assume this column differs between the platforms.

    def calc_revenue(self):
        return self.loan_amnt * np.power((1 + self.int_rate), self.term) - self.loan_amnt


class MyLCLoans(MyLoans):
    def __init__(self, df):
        super().__init__(df)
        self.int_rate = df["int_rate"]


class MyProsperLoans(MyLoans):
    def __init__(self, df):
        super().__init__(df)
        self.int_rate = df["intRate"]


def foo(loan: MyLoans):
    print(loan.calc_revenue())


if __name__ == '__main__':
    df = pd.DataFrame([[1000, 12, 0.3], [2500, 36, 0.1]])
    common_columns = ["loan_amnt", "term"]
    lc_df = df.copy()
    lc_df.columns = common_columns + ["int_rate"]
    prosper_df = df.copy()
    prosper_df.columns = common_columns + ["intRate"]

    foo(MyLCLoans(lc_df))
    foo(MyProsperLoans(prosper_df))