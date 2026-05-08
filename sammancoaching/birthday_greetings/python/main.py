import datetime
from dataclasses import dataclass


@dataclass
class Birthday:
    last_name: str
    first_name: str
    date_of_birth: datetime.date
    email: str


class BirthdayData:
    @staticmethod
    def load() -> list[Birthday]:
        pass


class Mailer:
    @staticmethod
    def mail(to: str, message: str):
        pass


class Matcher:
    @staticmethod
    def for_date(date: datetime.date, birthdays: list[Birthday]) -> list[Birthday]:
        return [
            x
            for x in birthdays
            if x.date_of_birth.month == date.month and x.date_of_birth.day == date.day
        ]


class BirthdayGreeter:
    def __init__(self, birthday_data: BirthdayData, mailer: Mailer):
        self.birthday_data = birthday_data
        self.mailer = mailer

    def greet(self):
        today = datetime.date.today()
        birthdays = self.birthday_data.load()
        matched = Matcher.for_date(today, birthdays)
        for bday in matched:
            subject = "Subject: Happy birthday!"
            body = f"Happy birthday, dear {bday.first_name}!"
            self.mailer.mail(bday.email, f"{subject}\n\n{body}")


def main():
    BirthdayGreeter(BirthdayData(), Mailer()).greet()


if __name__ == "__main__":
    main()
