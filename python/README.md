# Python Take-home Exercise

This is a simple Flask API for the take-home exercise.

## Getting Started

### Requirements

- Python 3.12 or later
- Required packages listed in pyproject.toml

### Installation

Ensure you have [`uv`](https://docs.astral.sh/uv/) installed (although using a different package manager is OK, if you prefer!).

### Running the Application

To start the application, run:

```sh
uv run gunicorn -b :8080 "src.app:create_app()"
```

The API will be available at `http://localhost:8080` and the mock service at `http://localhost:8888`.

## Available Endpoints

- `GET /`: Welcome message
- `GET /api/recipients`: Get all recipients
- `POST /api/submit`: Submit a recipient for processing

## Your Task

Please see the main readme file for detailed instructions!
