# test_app.py

import pytest

@pytest.fixture
def load_data():
    # Your data loading logic here
    return {"key": "value"}

def test_load_data(load_data):
    # Use the fixture as if it's a regular parameter
    assert load_data["key"] == "value"
