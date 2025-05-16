import requests
from flask import Flask  #, request

from src.mock_service.server import mock_service
from src.utils import initial_configuration


def create_app():
    app = Flask(__name__)
    state = initial_configuration()

    service = mock_service
    service.start()  # Start the mock service in a separate thread

    @app.route("/")
    def index():
        return "Good luck 💥!"

    # ********************
    # User Routes
    # ***

    @app.route("/api/users", methods=["GET"])
    def get_users():
        """
        Get all users endpoint.

        TODO(SHIP): Implement the user routes
        """
        pass

    @app.route("/api/users", methods=["POST"])
    def create_user():
        """
        Create a user endpoint.

        TODO(SHIP): Implement the user routes
        """
        pass

    # ********************
    # Resource Routes
    # ***

    @app.route("/api/recipients", methods=["GET"])
    def get_recipients():
        """Get all recipients endpoint."""
        return state["recipients"]

    @app.route("/api/submit", methods=["POST"])
    def submit_recipient():
        """
        Submit a recipient for processing endpoint.
        """
        # TODO(SHIP): Add rate limiting

        # body = request.json
        id_value = "fakeid"

        response = requests.post(
            f"{service.url}/process",
            headers={"Content-Type": "application/json"},
            json={"id": id_value},
        )

        return response.json(), response.status_code

    return app
