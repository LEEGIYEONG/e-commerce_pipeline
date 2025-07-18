
import os
import pandas as pd
import pytest
from toss_commerce_pipeline.scripts.generate_synthetic_data import generate_synthetic_data

@pytest.fixture
def setup_test_output():
    """Provide an output path for the test."""
    output_path = 'test_synthetic_data.parquet'
    yield output_path
    if os.path.exists(output_path):
        os.remove(output_path)

def test_generate_synthetic_data(setup_test_output):
    """Test the generate_synthetic_data function."""
    output_path = setup_test_output
    num_rows = 100
    generate_synthetic_data(output_path, num_rows)

    # Check if the output file is created
    assert os.path.exists(output_path)

    # Check the content of the output file
    df = pd.read_parquet(output_path)
    assert len(df) == num_rows
    expected_columns = ['timestamp', 'visitorid', 'itemid', 'event', 'transactionid', 'date']
    assert all(col in df.columns for col in expected_columns)
