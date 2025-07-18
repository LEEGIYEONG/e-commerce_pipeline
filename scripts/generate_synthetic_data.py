
import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

def generate_synthetic_data(output_path, num_rows=1000):
    """
    Generates synthetic e-commerce event data and saves it as a Parquet file.

    Args:
        output_path (str): The path to save the output Parquet file.
        num_rows (int): The number of synthetic data rows to generate.
    """
    fake = Faker()
    data = []
    events = ['view', 'addtocart', 'transaction']

    for _ in range(num_rows):
        timestamp = fake.date_time_between(start_date='-1y', end_date='now')
        visitor_id = fake.uuid4()
        item_id = random.randint(1, 100000)
        event = random.choices(events, weights=[0.7, 0.2, 0.1], k=1)[0]
        transaction_id = fake.uuid4() if event == 'transaction' else None

        data.append({
            'timestamp': timestamp,
            'visitorid': visitor_id,
            'itemid': item_id,
            'event': event,
            'transactionid': transaction_id,
            'date': timestamp.date()
        })

    df = pd.DataFrame(data)
    df.to_parquet(output_path, index=False)

if __name__ == '__main__':
    output_parquet_path = 'C:/Users/LEEGIYEONG/toss_commerce_pipeline/data/synthetic_events.parquet'
    generate_synthetic_data(output_parquet_path)
