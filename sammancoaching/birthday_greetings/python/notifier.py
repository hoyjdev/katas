from typing import Protocol


class Notifier(Protocol):
    def send(self, to: str, message: str) -> None: ...


class Mailer:
    def send(self, to: str, message: str) -> None:
        # Implementation for sending email
        pass
