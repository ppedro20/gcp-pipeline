#upload to GCS
from google.cloud import storage
import os 

client = storage.Client()
bucket = client.get_bucket('gcp-prj-bucket')

for file_path in ['../data/silver/movies_clean.parquet', '../data/gold/movies_agg.parquet']:
    blob = bucket.blob(os.path.basename(file_path))
    blob.upload_from_filename(file_path)
    print(f'File {file_path} uploaded to {bucket.name} as {blob.name}')
    
    