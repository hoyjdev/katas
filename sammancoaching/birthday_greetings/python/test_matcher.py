import datetime

from birthday import Birthday
from matcher import Matcher


class TestMatcher:
    def test_partitions_birthdays_and_non_birthdays_for_given_date(self, john, mary):
        date = datetime.date(2023, 1, 1)
        assert Matcher.for_date(date, [john, mary]) == ([john], [mary])

    def test_returns_leap_day_birthdays_given_date_is_feb_28(self, john, mary):
        leaper = Birthday(
            "Jones", "Leaper", datetime.date(2020, 2, 29), "leaper.jones@example.com"
        )
        date = datetime.date(2023, 2, 28)
        assert Matcher.for_date(date, [john, mary, leaper]) == ([leaper], [john, mary])
