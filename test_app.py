import pandas as pd
import pytest

# Define a fixture for loading data
@pytest.fixture
def load_data():
    data_path = 'data/units_data.csv'
    df = pd.read_csv(data_path)
    df.columns = df.columns.str.strip()  # Remove any leading/trailing spaces from column names
    return df

# Sample test to check if the data loading function works correctly
def test_load_data(load_data):
    df = load_data
    assert not df.empty, "DataFrame should not be empty"
    assert 'Building' in df.columns, "DataFrame should have a 'Building' column"
