import string
import random
from faker import Faker
from src.types import Recipient, User

faker = Faker()


def create_fake_recipient() -> Recipient:
    """Create a fake recipient with realistic data."""
    return Recipient(
        name=faker.name(),
        email=faker.email(),
        created=faker.date_time_this_decade(),
        updated=faker.date_time_this_month(),
        image_url=faker.image_url(width=300, height=300),
    )


def generate_access_token(length: int = 20) -> str:
    """Generate a random alphanumeric access token."""
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for _ in range(length))


def generate_fake_user() -> User:
    """Create a fake user with realistic data."""
    return User(
        name=faker.name(),
        email=faker.email(),
        created=faker.date_time_this_decade(),
        updated=faker.date_time_this_month(),
        access_token=generate_access_token(),
    )
