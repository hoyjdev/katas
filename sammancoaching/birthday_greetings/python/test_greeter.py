import freezegun
import mock
from pytest import fixture

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
            )
        ]
