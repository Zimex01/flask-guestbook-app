from app.main import app, sanitize_input
import pytest

def test_index():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"Guestbook" in response.data

def test_sanitize_input():
    assert sanitize_input("Hello<script>!") == "Hello"
    assert sanitize_input("a" * 60) == "a" * 50
    assert sanitize_input("") == ""