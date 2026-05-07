from dataclasses import dataclass
from datetime import date


class BankAccount:
    def __init__(self):
        self.transactions = []

    def deposit(self, amount: int) -> None:
        self.transactions = self.transactions + [
            Banker.transact(self.transactions[-1].balance, amount, date.today())
        ]

    def withdraw(self, amount: int) -> None:
        self.transactions = self.transactions + [
            Banker.transact(self.transactions[-1].balance, -amount, date.today())
        ]

    def printStatement(self) -> None:
        # When you call the ‘printStatement’ method, something like the following is printed on standard output:

        # Date       || Amount || Balance
        # 2012-01-14 || -500   || 2500
        # 2012-01-13 || 2000   || 3000
        # 2012-01-10 || 1000   || 1000

        # This example statement shows one withdrawal on 14th January 2012, and two deposits on 13th and 10th January respectively.
        pass


@dataclass
class Transaction:
    amount: int
    balance: int
    date: date = date.today()


class Banker:
    @staticmethod
    def transact(balance: int, amount: int, date: date) -> Transaction:
        return Transaction(amount, balance + amount, date)


def main():
    print("Hello from python!")


if __name__ == "__main__":
    main()
