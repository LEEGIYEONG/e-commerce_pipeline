
import pandas as pd

def preprocess_events(input_path, output_path):
    """
    Preprocesses the events data from a CSV file and saves it as a Parquet file.

    Args:
        input_path (str): The path to the input CSV file.
        output_path (str): The path to save the output Parquet file.
    """
    # Read the events data
    events_df = pd.read_csv(input_path)

    # Convert the 'timestamp' column to datetime objects
    events_df['timestamp'] = pd.to_datetime(events_df['timestamp'], unit='ms')

    # Add a 'date' column
    events_df['date'] = events_df['timestamp'].dt.date

    # Save the preprocessed data as a Parquet file
    events_df.to_parquet(output_path, index=False)

if __name__ == '__main__':
    # Define the input and output paths
    input_csv_path = 'C:/Users/LEEGIYEONG/toss_commerce_pipeline/data/events.csv'
    output_parquet_path = 'C:/Users/LEEGIYEONG/toss_commerce_pipeline/data/preprocessed_events.parquet'

    # Run the preprocessing function
    preprocess_events(input_csv_path, output_parquet_path)
