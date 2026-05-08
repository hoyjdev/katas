import datetime

from birthday import BirthdayData
from matcher import Matcher
from notifier import Notifier


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
