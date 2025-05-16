import random
import time
import threading
from flask import Flask, request
from src.mock_service.limiter import limiter

# Define the port for the mock service
mock_port = 8888

# Create the Flask app
mock_app = Flask(__name__)
limiter.init_app(mock_app)


class MockService:
    """A mock service that simulates a real API integration."""

    def __init__(self):
        self.url = f"http://localhost:{mock_port}"
        self._server_thread = None

    def start(self):
        """Start the mock service in a separate thread."""
        if self._server_thread is None:
            self._server_thread = threading.Thread(
                target=lambda: mock_app.run(
                    host="0.0.0.0", port=mock_port, debug=False, use_reloader=False
                )
            )
            self._server_thread.daemon = True
            self._server_thread.start()
            print(f"ℹ️ Mock service has started at {self.url}")

    def stop(self):
        """Stop the mock service."""
        # Flask doesn't provide a clean way to stop the server programmatically
        # In a real implementation, we would run both apps separately using docker compose
        pass


# Create the mock service instance
mock_service = MockService()


@mock_app.route("/", methods=["GET"])
def index():
    """Root endpoint for the mock service."""
    return "Mock Service: Good luck!"


@mock_app.route("/process", methods=["POST"])
@limiter.limit("20 per 30seconds")
def process():
    """Process endpoint that will intentionally fail some requests."""
    data = request.json

    # Get id from request
    id_value = data.get("id")

    # Make sure id exists
    if not id_value:
        return {"message": "Id is required"}, 400

    # Return a 500 response 20% of the time to simulate a server error
    if random.random() > 0.8:
        return {"message": "Internal server error, please retry"}, 500

    # 10% of the time, delay the request by 10 seconds to simulate a slow server
    if random.random() > 0.9:
        time.sleep(10)

    return {"status": "processed"}
