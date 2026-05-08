import datetime
from dataclasses import dataclass


@dataclass
class Birthday:
    last_name: str
    first_name: str
    date_of_birth: datetime.date
    email: str


class BirthdayData:
    @staticmethod
    def load() -> list[Birthday]:
        # Can be local file, DB, whatever
        pass
