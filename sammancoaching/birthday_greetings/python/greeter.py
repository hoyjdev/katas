import datetime

from birthday import BirthdayData
from matcher import Matcher
from notifier import Notifier

# TODO:
# - clean up message creation
# - simplify BirthdayGreeter core/shell boundaries


class BirthdayGreeter:
    def __init__(self, birthday_data: BirthdayData, notifier: Notifier):
        self.birthday_data = birthday_data
        self.notifier = notifier

    def greet(self):
        today = datetime.date.today()
        birthdays = self.birthday_data.load()
        matched, unmatched = Matcher.for_date(today, birthdays)

        for bday in matched:
            subject = "Subject: Happy birthday!"
            body = f"Happy birthday, dear {bday.first_name}!"
            self.notifier.send(bday.email, f"{subject}\n\n{body}")

        names = [f"{m.first_name} {m.last_name}" for m in matched]
        joined_names = self._join_names(names)
        suffix = "birthday" if len(matched) == 1 else "birthdays"

        for bday in unmatched:
            subject = "Subject: Birthday Reminder"
            body = (
                f"Dear {bday.first_name},\n\n"
                f"Today is {joined_names}'s {suffix}.\n"
                "Don't forget to send them each a message!"
            )
            self.notifier.send(bday.email, f"{subject}\n\n{body}")

    def _join_names(self, names: list[str]) -> str:
        if len(names) <= 2:
            return " and ".join(names)
        return f"{', '.join(names[:-1])} and {names[-1]}"
