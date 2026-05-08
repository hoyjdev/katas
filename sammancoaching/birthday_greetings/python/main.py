from birthday import BirthdayData
from greeter import BirthdayGreeter
from notifier import Mailer


def main():
    BirthdayGreeter(BirthdayData(), Mailer()).greet()


if __name__ == "__main__":
    main()
