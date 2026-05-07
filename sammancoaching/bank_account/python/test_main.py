import datetime

from main import BankAccount, Banker, Transaction

# BankAccount:
# - it has a balance to keep track of the money in the account
# - it deposits money into the account
# - it withdraws money from the account
# - it prints a statement of all transactions
#
# BankAccount is the outer shell. Banker is the core that sees/manipulates balance.
# "DB" -> BankAccount -> Banker -> BankAccount -> console (printStatement)
#
# Kata restricts changing BankAccount public interface. Design according to rules then
# refactor into something cleaner if possible (core/shell split)


# class TestBankAccount:
#     def test_tracks_deposits(self):
#         account = BankAccount()
#         account.deposit(1000)
#         assert account.transactions == [("", 1000, 1000)]


class TestTransaction:
    def test_has_date(self):
        txn = Transaction(1000, 2000, datetime.date(2023, 1, 1))
        assert txn.date == datetime.date(2023, 1, 1)

    def test_has_amount(self):
        txn = Transaction(1000, 2000, datetime.date(2023, 1, 1))
        assert txn.amount == 1000

    def test_has_balance(self):
        txn = Transaction(1000, 2000, datetime.date(2023, 1, 1))
        assert txn.balance == 2000


class TestBanker:
    def test_returns_date_and_balance_after_transaction(self):
        actual = Banker.transact(0, 1000, datetime.date(2023, 1, 1))
        assert actual == Transaction(1000, 1000, datetime.date(2023, 1, 1))

    def test_subtracts_money_from_the_balance(self):
        actual = Banker.transact(3000, -500, datetime.date(2023, 1, 1))
        assert actual == Transaction(-500, 2500, datetime.date(2023, 1, 1))
