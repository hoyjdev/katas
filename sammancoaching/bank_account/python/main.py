from dataclasses import dataclass
from datetime import datetime
from time import sleep


class BankAccount:
    def __init__(self):
        self.transactions = []

    def deposit(self, amount: int) -> None:
        self.transactions = self.transactions + [
            Banker.transact(self.transactions, amount, datetime.today())
        ]

    def withdraw(self, amount: int) -> None:
        self.transactions = self.transactions + [
            Banker.transact(self.transactions, -amount, datetime.today())
        ]

    def printStatement(self) -> None:
        print(Statement.for_txns(self.transactions))


@dataclass
class Transaction:
    amount: int
    balance: int
    timestamp: datetime = datetime.today()


class Banker:
    @staticmethod
    def transact(txns: list[Transaction], amount: int, ts: datetime) -> Transaction:
        if not txns:
            return Transaction(amount, amount, ts)

        return Transaction(amount, txns[-1].balance + amount, ts)


class Statement:
    @staticmethod
    def for_txns(txns: list[Transaction]) -> str:
        sorted_txns = sorted(txns, key=lambda t: t.timestamp, reverse=True)
        print_outs = [
            f"{datetime.strftime(t.timestamp, '%Y-%m-%d')},{t.amount},{t.balance}\n"
            for t in sorted_txns
        ]
        return "Date,Amount,Balance\n" + "".join(print_outs)


def main():
    account = BankAccount()
    account.deposit(1000)
    sleep(1)
    account.deposit(2000)
    sleep(1)
    account.withdraw(500)
    sleep(1)
    account.printStatement()


if __name__ == "__main__":
    main()
