import datetime
from dataclasses import dataclass
from typing import Protocol


@dataclass
class Birthday:
    last_name: str
    first_name: str
    date_of_birth: datetime.date
    email: str


class BirthdayData:
    @staticmethod
    def load() -> list[Birthday]:
        # Can be local file, DB, whatever
        pass


class Notifier(Protocol):
    def send(self, to: str, message: str) -> None: ...


class Mailer:
    def send(self, to: str, message: str) -> None:
        # Implementation for sending email
        pass


class Matcher:
    @staticmethod
    def for_date(date: datetime.date, birthdays: list[Birthday]) -> list[Birthday]:
        targets = {(date.month, date.day)}
        if (date.month, date.day) == (2, 28):
            targets.add((2, 29))

        return [
            b
            for b in birthdays
            if (b.date_of_birth.month, b.date_of_birth.day) in targets
        ]


class BirthdayGreeter:
    def __init__(self, birthday_data: BirthdayData, notifier: Notifier):
        self.birthday_data = birthday_data
        self.notifier = notifier

    def greet(self):
        today = datetime.date.today()
        birthdays = self.birthday_data.load()
        matched = Matcher.for_date(today, birthdays)
        for bday in matched:
            subject = "Subject: Happy birthday!"
            body = f"Happy birthday, dear {bday.first_name}!"
            self.notifier.send(bday.email, f"{subject}\n\n{body}")


def main():
    BirthdayGreeter(BirthdayData(), Mailer()).greet()


if __name__ == "__main__":
    main()
