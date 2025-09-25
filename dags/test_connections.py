from datetime import datetime
from airflow import DAG
from airflow.decorators import task

from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from airflow.providers.google.cloud.hooks.gcs import GCSHook
from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator

BUCKET = "meu-bucket-dados12433"      # ajuste
BQ_PROJECT = "ambient-elf-472302-i1"        # ajuste
BQ_LOCATION = "US"                # ajuste

with DAG(
    dag_id="test_snowflake_gcp_connections",
    start_date=datetime(2025, 1, 1),
    schedule=None,  # <-- Changed from schedule_interval
    catchup=False,
    tags=["test", "infra"],
) as dag:

    @task
    def test_snowflake():
        sf = SnowflakeHook(snowflake_conn_id="snowflake_default")
        # teste rápido
        row = sf.get_first("SELECT 1")
        print("Snowflake SELECT 1 =>", row)

    @task
    def test_gcs_upload():
        gcs = GCSHook(gcp_conn_id="google_cloud_default")
        content = b"airflow connection test"
        obj = "tmp/airflow_connection_test.txt"
        gcs.upload(bucket_name=BUCKET, object_name=obj, data=content)
        print(f"Uploaded gs://{BUCKET}/{obj}")

    test_bq = BigQueryInsertJobOperator(
        task_id="test_bigquery_query",
        gcp_conn_id="google_cloud_default",
        configuration={
            "query": {
                "query": "SELECT 1 AS ok",
                "useLegacySql": False
            }
        },
        location=BQ_LOCATION,
        project_id=BQ_PROJECT,
    )

    @task
    def create_table_if_not_exists():
        """Create the table if it doesn't exist"""
        bq_hook = BigQueryHook(gcp_conn_id="google_cloud_default")
        
        # Create table SQL
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS `ambient-elf-472302-i1.demo_dataset.customer_data` (
            customer_id INT64,
            name STRING,
            email STRING,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP()
        )
        """
        
        # Get the BigQuery client and execute the SQL
        client = bq_hook.get_client()
        query_job = client.query(create_table_sql)
        query_job.result()  # Wait for the job to complete
        
        print("Table created successfully!")

    @task
    def insert_data_with_hook():
        bq_hook = BigQueryHook(gcp_conn_id="google_cloud_default")
        
        # Data to insert
        data = [
            {"customer_id": 1, "name": "John Doe", "email": "john@example.com"},
            {"customer_id": 2, "name": "Jane Smith", "email": "jane@example.com"},
        ]
        
        # Insert data
        bq_hook.insert_all(
            project_id="ambient-elf-472302-i1",
            dataset_id="demo_dataset",
            table_id="customer_data",
            rows=data
        )
        
        print("Data inserted successfully!")

    # Update the task chain
    test_snowflake() >> test_gcs_upload() >> test_bq >> create_table_if_not_exists() >> insert_data_with_hook()
