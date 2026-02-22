import pytest

from app import app as flask_app


def test_root_returns_200_and_message():
    client = flask_app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.get_json()
    assert data["message"] == "Hello, World!"
