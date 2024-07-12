import pandas as pd
import pytest

# Sample test to check if the data loading function works correctly
def test_load_data():
    # Assuming the CSV file contains a column named 'Building'
    data_path = 'data/units_data.csv'
    
    @pytest.fixture
    def load_data():
        df = pd.read_csv(data_path)
        df.columns = df.columns.str.strip()  # Remove any leading/trailing spaces from column names
        return df

    df = load_data()
    assert not df.empty, "DataFrame should not be empty"
    assert 'Building' in df.columns, "DataFrame should have a 'Building' column"
