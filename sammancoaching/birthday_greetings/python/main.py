import datetime
from dataclasses import dataclass


@dataclass
class Birthday:
    first_name: str
    last_name: str
    date_of_birth: str
    email: str


class BirthdayData:
    @staticmethod
    def load() -> list[Birthday]:
        pass


class Mailer:
    @staticmethod
    def mail(to: str, message: str):
        pass


class BirthdayGreeter:
    def __init__(self, birthday_data: BirthdayData, mailer: Mailer):
        self.birthday_data = birthday_data
        self.mailer = mailer

    def greet(self):
        today = datetime.date.today()
        birthdays = self.birthday_data.load()
        for bday in birthdays:
            # Parsing date_of_birth (expecting YYYY-MM-DD or YYYY/MM/DD)
            # The test uses YYYY-MM-DD
            dob = datetime.datetime.strptime(
                bday.date_of_birth.replace("/", "-"), "%Y-%m-%d"
            ).date()
            if dob.month == today.month and dob.day == today.day:
                subject = "Subject: Happy birthday!"
                body = f"Happy birthday, dear {bday.first_name}!"
                self.mailer.mail(bday.email, f"{subject}\n\n{body}")


def main():
    BirthdayGreeter(BirthdayData(), Mailer()).greet()


if __name__ == "__main__":
    main()
