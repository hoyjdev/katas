import datetime

import freezegun
import mock
from pytest import fixture

from birthday import Birthday
from greeter import BirthdayGreeter


@fixture
def mailer():
    with mock.patch("notifier.Mailer") as mock_svc:
        yield mock_svc


@fixture
def birthday_data():
    with mock.patch("birthday.BirthdayData") as mock_svc:
        yield mock_svc


class TestBirthdayGreeter:
    @freezegun.freeze_time("2023-01-01")
    def test_sends_emails_on_birthday(self, birthday_data, john, mary, mailer):
        birthday_data.load.return_value = [john, mary]

        BirthdayGreeter(birthday_data, mailer).greet()

        assert mailer.send.call_args_list == [
            mock.call(
                "john.doe@example.com",
                "Subject: Happy birthday!\n\nHappy birthday, dear John!",
            ),
            mock.call(
                "mary.ann@example.com",
                (
                    "Subject: Birthday Reminder\n\n"
                    "Dear Mary,\n\n"
                    "Today is John Doe's birthday.\n"
                    "Don't forget to send them each a message!"
                ),
            ),
        ]

    @freezegun.freeze_time("2023-01-01")
    def test_sends_reminder_to_friends_about_others_birthdays(
        self, birthday_data, john, mary, mailer
    ):
        peter = Birthday(
            "Pan", "Peter", datetime.date(1980, 1, 1), "peter.pan@example.com"
        )
        stuart = Birthday(
            "Little", "Stuart", datetime.date(1985, 2, 1), "stuart.little@example.com"
        )
        birthday_data.load.return_value = [john, mary, peter, stuart]

        BirthdayGreeter(birthday_data, mailer).greet()

        assert mailer.send.call_args_list == [
            mock.call(
                "john.doe@example.com",
                "Subject: Happy birthday!\n\nHappy birthday, dear John!",
            ),
            mock.call(
                "peter.pan@example.com",
                "Subject: Happy birthday!\n\nHappy birthday, dear Peter!",
            ),
            mock.call(
                "mary.ann@example.com",
                (
                    "Subject: Birthday Reminder\n\n"
                    "Dear Mary,\n\n"
                    "Today is John Doe and Peter Pan's birthdays.\n"
                    "Don't forget to send them each a message!"
                ),
            ),
            mock.call(
                "stuart.little@example.com",
                (
                    "Subject: Birthday Reminder\n\n"
                    "Dear Stuart,\n\n"
                    "Today is John Doe and Peter Pan's birthdays.\n"
                    "Don't forget to send them each a message!"
                ),
            ),
        ]
