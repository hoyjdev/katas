class BankAccount:
    def deposit(self, amount: int) -> None:
        pass

    def withdraw(self, amount: int) -> None:
        pass

    def printStatement(self) -> None:
        # When you call the ‘printStatement’ method, something like the following is printed on standard output:

        # Date       || Amount || Balance
        # 2012-01-14 || -500   || 2500
        # 2012-01-13 || 2000   || 3000
        # 2012-01-10 || 1000   || 1000

        # This example statement shows one withdrawal on 14th January 2012, and two deposits on 13th and 10th January respectively.
        pass


def main():
    print("Hello from python!")


if __name__ == "__main__":
    main()
