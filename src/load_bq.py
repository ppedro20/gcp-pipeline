#Load Data to BigQuery
from google.cloud import bigquery

client = bigquery.Client()
dataset_id = 'pipeline_dataset'

table_id = f'{dataset_id}.sales'

job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.PARQUET,
    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
)

uri = 'gs://gcp-prj-bucket/Coffe_sales.parquet'
load_job = client.load_table_from_uri(uri, table_id, job_config=job_config)
load_job.result()  # Waits for the job to complete.

