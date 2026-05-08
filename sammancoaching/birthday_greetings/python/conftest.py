import datetime

from pytest import fixture

from birthday import Birthday


@fixture
def john():
    return Birthday("Doe", "John", datetime.date(1990, 1, 1), "john.doe@example.com")


@fixture
def mary():
    return Birthday("Ann", "Mary", datetime.date(1975, 9, 11), "mary.ann@example.com")
