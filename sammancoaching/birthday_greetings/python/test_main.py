import datetime

import freezegun
import mock
from pytest import fixture

from main import Birthday, BirthdayGreeter, Matcher

# Birthday Greetings Kata
# Imagine you have a flat file with all your friends’ birthdays:

# last_name, first_name, date_of_birth, email
# Doe, John, 1982/10/08, john.doe@example.com
# Ann, Mary, 1975/09/11, mary.ann@example.com

# You would like to send them an email on their birthday:

# ===
# Subject: Happy birthday!

# Happy birthday, dear <first_name>!
# ===
# Shell -> Core -> Shell
# load and parse the birthdays -> identify birthdays, create messages -> send in email

# 1. Loading Birthdays (Shell)
# - Should read 'birthdays.csv' and parse its contents.
# - Handle various date formats or potential CSV malformation? No. Keep it simple

# 2. Identifying Birthdays (Core)
# - Given 'today's date', identify all individuals whose month and day match.
# - Special Case: Leap years, send on Feb 28th.

# 3. Message Formatting (Core)
# - For each person identified, generate a message.
# - Subject: Happy birthday!
# - Body: Happy birthday, dear <first_name>!

# 4. "Sending" the Email (Shell)
# - Since we aren't sending real emails, we need an abstraction (e.g., an EmailService or a port).
# - Tests should verify that the service's 'send' method is called with the correct recipient and content.

# 5. Execution Flow (The 'main' logic)
# - main() should orchestrate:
#   a) Getting the current date.
#   b) Reading the CSV.
#   c) Filtering birthdays.
#   d) Passing messages to the sender.
#


@fixture
def mailer():
    with mock.patch("main.Mailer") as mock_svc:
        yield mock_svc


@fixture
def birthday_data():
    with mock.patch("main.BirthdayData") as mock_svc:
        yield mock_svc


class TestBirthdayGreeter:
    @freezegun.freeze_time("2023-01-01")
    def test_sends_emails_on_birthday(self, birthday_data, mailer):
        birthday_data.load.return_value = [
            Birthday("Doe", "John", datetime.date(1990, 1, 1), "john.doe@example.com"),
            Birthday("Ann", "Mary", datetime.date(1975, 9, 11), "mary.ann@example.com"),
        ]

        BirthdayGreeter(birthday_data, mailer).greet()

        assert mailer.mail.call_args_list == [
            mock.call(
                "john.doe@example.com",
                "Subject: Happy birthday!\n\nHappy birthday, dear John!",
            )
        ]


class TestMatcher:
    def test_returns_birthdays_that_match_given_date(self):
        john = Birthday(
            "Doe", "John", datetime.date(1990, 1, 1), "john.doe@example.com"
        )
        mary = Birthday(
            "Ann", "Mary", datetime.date(1975, 9, 11), "mary.ann@example.com"
        )
        assert Matcher.for_date(datetime.date(2023, 1, 1), [john, mary]) == [john]

    # def test_returns_leap_day_birthdays_given_date_is_feb_28(self):
    #     john = Birthday(
    #         "Doe", "John", datetime.date(1990, 1, 1), "john.doe@example.com"
    #     )
    #     mary = Birthday(
    #         "Ann", "Mary", datetime.date(2020, 2, 29), "mary.ann@example.com"
    #     )
    #     assert Matcher.for_date(datetime.date(2023, 2, 28), [john, mary]) == [mary]
