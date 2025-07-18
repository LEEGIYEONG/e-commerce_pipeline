

# Toss Commerce Data Pipeline Project

This project is a data engineering pipeline for a fictional Toss Commerce service, inspired by a job posting for a Data Engineer at Toss. The goal is to build a robust and scalable data pipeline that processes e-commerce event data, enriches it, and prepares it for various downstream applications such as business intelligence, analytics, and machine learning.

## Project Structure

```
toss_commerce_pipeline/
├── dags/
│   ├── __init__.py
│   └── process_events_dag.py
├── data/
│   ├── category_tree.csv
│   ├── events.csv
│   ├── item_properties_part1.csv
│   ├── item_properties_part2.csv
│   ├── preprocessed_events.parquet
│   └── synthetic_events.parquet
├── scripts/
│   ├── __init__.py
│   ├── generate_synthetic_data.py
│   └── preprocess_events.py
├── tests/
│   ├── __init__.py
│   ├── test_generate_synthetic_data.py
│   └── test_preprocess_events.py
├── __init__.py
└── README.md
```

## Data Schema

The primary dataset used in this project is the [Retailrocket recommender system dataset](https://www.kaggle.com/retailrocket/ecommerce-dataset). The main `events.csv` file has the following schema:

| Column        | Type      | Description                                                                   |
|---------------|-----------|-------------------------------------------------------------------------------|
| `timestamp`   | `int64`   | The timestamp of the event in milliseconds since the epoch.                   |
| `visitorid`   | `int64`   | A unique identifier for the visitor.                                          |
| `itemid`      | `int64`   | A unique identifier for the item.                                             |
| `event`       | `string`  | The type of event (e.g., 'view', 'addtocart', 'transaction').                |
| `transactionid`| `float64` | The ID of the transaction, if the event is a transaction. Otherwise, NaN.     |

After preprocessing, the following columns are added:

| Column      | Type       | Description                                       |
|-------------|------------|---------------------------------------------------|
| `timestamp` | `datetime64[ns]` | The timestamp of the event as a datetime object.  |
| `date`      | `object` (date) | The date of the event.                            |

## Data Pipeline Logic

The data pipeline is designed to be executed as a DAG (Directed Acyclic Graph) in a workflow management tool like Apache Airflow. The main steps are:

1.  **Ingest Raw Data:** The pipeline starts by ingesting the raw `events.csv` data.
2.  **Preprocess Data:** The `preprocess_events.py` script performs the following transformations:
    *   Converts the `timestamp` column from milliseconds to a datetime object.
    *   Adds a `date` column for partitioning and easier time-based analysis.
    *   Saves the processed data in Parquet format for efficient storage and querying.
3.  **Generate Synthetic Data (Optional):** The `generate_synthetic_data.py` script can be used to generate additional, synthetic event data. This is useful for testing the pipeline at scale and for developing new features when real data is limited.
4.  **Load to Data Warehouse:** The processed data (both real and synthetic) is then ready to be loaded into a data warehouse (e.g., BigQuery, Redshift, Snowflake) for further analysis.

### Data Flow Diagram

```mermaid
graph TD
    A[Raw Data (events.csv)] --> B{Preprocess Events};
    B --> C[Preprocessed Data (preprocessed_events.parquet)];
    D[Synthetic Data Generation] --> E[Synthetic Data (synthetic_events.parquet)];
    C --> F[Data Warehouse];
    E --> F;
    F --> G[BI & Analytics];
    F --> H[Machine Learning];
```

## Getting Started

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd toss_commerce_pipeline
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Download the data:**
    *   Install the Kaggle API: `pip install kaggle`
    *   Download your `kaggle.json` API token from your Kaggle account settings.
    *   Place the `kaggle.json` file in `~/.kaggle/` (for Linux/macOS) or `C:\Users\<Your-Username>\.kaggle\` (for Windows).
    *   Run the following command to download and unzip the data:
        ```bash
        kaggle datasets download -d retailrocket/ecommerce-dataset -p data --unzip
        ```

4.  **Run the preprocessing script:**
    ```bash
    python scripts/preprocess_events.py
    ```

5.  **Run the tests:**
    ```bash
    pytest
    ```

## Future Work

*   **Data Warehouse Integration:** Add a step to the pipeline to load the processed data into a data warehouse like BigQuery or Snowflake.
*   **Real-time Processing:** Implement a real-time data processing pipeline using Kafka and Spark Streaming or Flink.
*   **Recommendation System:** Build a product recommendation model based on the processed data.
*   **CI/CD:** Set up a CI/CD pipeline using GitHub Actions to automate testing and deployment.
*   **Containerization:** Dockerize the application for easier deployment and scalability.

