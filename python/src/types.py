from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    name: str
    email: str
    created: datetime
    updated: datetime
    access_token: str


@dataclass
class Recipient:
    name: str
    email: str
    created: datetime
    updated: datetime
    image_url: str


@dataclass
class State:
    recipients: list[Recipient]
    users: list[User]
