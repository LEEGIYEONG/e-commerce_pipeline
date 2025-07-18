
import os
import pandas as pd
import pytest
from toss_commerce_pipeline.scripts.preprocess_events import preprocess_events

@pytest.fixture
def setup_test_data():
    """Create a dummy CSV file for testing."""
    data = {
        'timestamp': [1433221332116, 1433221332117, 1433221332118],
        'visitorid': [1, 2, 3],
        'itemid': [10, 20, 30],
        'event': ['view', 'addtocart', 'transaction'],
        'transactionid': [None, None, 't123']
    }
    df = pd.DataFrame(data)
    input_path = 'test_input.csv'
    output_path = 'test_output.parquet'
    df.to_csv(input_path, index=False)
    yield input_path, output_path
    os.remove(input_path)
    os.remove(output_path)

def test_preprocess_events(setup_test_data):
    """Test the preprocess_events function."""
    input_path, output_path = setup_test_data
    preprocess_events(input_path, output_path)

    # Check if the output file is created
    assert os.path.exists(output_path)

    # Check the content of the output file
    processed_df = pd.read_parquet(output_path)
    assert not processed_df.empty
    assert 'date' in processed_df.columns
    assert pd.api.types.is_datetime64_any_dtype(processed_df['timestamp'])
