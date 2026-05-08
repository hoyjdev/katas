import datetime

import freezegun
import mock
from pytest import fixture

from birthday import Birthday
from greeter import BirthdayGreeter
from matcher import Matcher


@fixture
def mailer():
    with mock.patch("notifier.Mailer") as mock_svc:
        yield mock_svc


@fixture
def birthday_data():
    with mock.patch("birthday.BirthdayData") as mock_svc:
        yield mock_svc


@fixture
def john():
    return Birthday("Doe", "John", datetime.date(1990, 1, 1), "john.doe@example.com")


@fixture
def mary():
    return Birthday("Ann", "Mary", datetime.date(1975, 9, 11), "mary.ann@example.com")


class TestBirthdayGreeter:
    @freezegun.freeze_time("2023-01-01")
    def test_sends_emails_on_birthday(self, birthday_data, john, mary, mailer):
        birthday_data.load.return_value = [john, mary]

        BirthdayGreeter(birthday_data, mailer).greet()

        assert mailer.send.call_args_list == [
            mock.call(
                "john.doe@example.com",
                "Subject: Happy birthday!\n\nHappy birthday, dear John!",
            )
        ]


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
