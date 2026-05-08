import datetime

from birthday import Birthday


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
