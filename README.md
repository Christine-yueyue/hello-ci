# hello-ci

Created for a minimal CI/demo use case.

This repository contains a single-route Flask app that returns a JSON greeting and a small pytest test suite. It's a CI smoke-test, demonstration, and a start point for a microservice.

## What it does

- Serves a JSON response at `/` with {"message": "Hello, World!"}.
- Includes one pytest test to verify the root route and response content.
- A `Dockerfile` is provided to build a small container image that runs the app.

## Requirements

- Python 3.11 (tested)
- See `requirements.txt` for pinned packages (`flask==3.0.3`, `pytest`).

## Run locally

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Start the app:

```bash
python app.py
```

The app will listen on port 8000 by default. Visit http://127.0.0.1:8000/ to see the JSON response.

## Run tests

```bash
pytest -q
```

## Docker

Build and run the containerized app:

```bash
docker build -t hello-ci:latest .
docker run -p 8000:8000 hello-ci:latest
```