import os
import json
from src.types import State
from src.mocks.mocker import create_fake_recipient, generate_fake_user


def initial_configuration() -> State:
    """
    Load existing recipients or create new ones.

    This function tries to load recipients from a JSON file. If the file doesn't exist,
    it creates default data with fake recipients and users.

    Returns:
        State: The application state with recipients and users
    """
    data_dir = os.path.join("src", "data")
    file_path = os.path.join(data_dir, "recipients.json")

    # Create directory and file if they don't exist
    try:
        with open(file_path, "r") as f:
            pass
    except (FileNotFoundError, IOError):
        os.makedirs(data_dir, exist_ok=True)
        with open(file_path, "w") as f:
            f.write("{}")

    save = False

    # Load data from file or create an empty state
    try:
        with open(file_path, "r") as f:
            obj = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        obj = {}

    # Create recipients if they don't exist
    if "recipients" not in obj:
        recipients = [create_fake_recipient() for _ in range(30)]
        # Convert to dictionaries for JSON serialization
        obj["recipients"] = [
            {
                "name": r.name,
                "email": r.email,
                "created": r.created.isoformat(),
                "updated": r.updated.isoformat(),
                "image_url": r.image_url,
            }
            for r in recipients
        ]
        save = True

    # Create users if they don't exist
    if "users" not in obj:
        user = generate_fake_user()
        obj["users"] = [
            {
                "name": user.name,
                "email": user.email,
                "created": user.created.isoformat(),
                "updated": user.updated.isoformat(),
                "access_token": user.access_token,
            }
        ]
        save = True

    # Save updated data if needed
    if save:
        with open(file_path, "w") as f:
            json.dump(obj, f, indent=2)

    # Return the state object (this will require deserialization in a real app)
    # For simplicity, we're just returning the dictionary here
    return obj
