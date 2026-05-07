import datetime

from main import Banker, Statement, Transaction

# BankAccount:
# - it has a record of transactions
# - it deposits money into the account
# - it withdraws money from the account
# - it prints a statement of all transactions


class TestTransaction:
    def test_has_date(self):
        txn = Transaction(1000, 2000, datetime.datetime(2023, 1, 1))
        assert txn.timestamp == datetime.date(2023, 1, 1)

    def test_has_amount(self):
        txn = Transaction(1000, 2000, datetime.datetime(2023, 1, 1))
        assert txn.amount == 1000

    def test_has_balance(self):
        txn = Transaction(1000, 2000, datetime.datetime(2023, 1, 1))
        assert txn.balance == 2000


class TestBanker:
    def test_returns_date_and_balance_after_transaction(self):
        actual = Banker.transact([], 1000, datetime.datetime(2023, 1, 1))
        assert actual == Transaction(1000, 1000, datetime.datetime(2023, 1, 1))

    def test_subtracts_money_from_the_balance(self):
        txns = [Transaction(2000, 3000, datetime.datetime(2023, 1, 1))]
        actual = Banker.transact(txns, -500, datetime.datetime(2023, 1, 1))
        assert actual == Transaction(-500, 2500, datetime.datetime(2023, 1, 1))


class TestStatement:
    def test_contains_header_as_first_item(self):
        assert Statement.for_txns([]) == "Date,Amount,Balance\n"

    def test_sorts_transactions_by_date_descending(self):
        txns = [
            Transaction(2000, 3000, datetime.datetime(2012, 1, 13)),
            Transaction(1000, 1000, datetime.datetime(2012, 1, 10)),
            Transaction(-500, 2500, datetime.datetime(2012, 1, 14)),
        ]
        assert (
            Statement.for_txns(txns) == "Date,Amount,Balance\n"
            "2012-01-14,-500,2500\n"
            "2012-01-13,2000,3000\n"
            "2012-01-10,1000,1000\n"
        )
