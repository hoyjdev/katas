import datetime

from birthday import Birthday
from matcher import Matcher


class TestMatcher:
    def test_returns_birthdays_that_match_given_date(self, john, mary):
        assert Matcher.for_date(datetime.date(2023, 1, 1), [john, mary]) == [john]

    def test_returns_leap_day_birthdays_given_date_is_feb_28(self, john, mary):
        leaper = Birthday(
            "Jones", "Leaper", datetime.date(2020, 2, 29), "leaper.jones@example.com"
        )
        assert Matcher.for_date(datetime.date(2023, 2, 28), [john, mary, leaper]) == [
            leaper
        ]
