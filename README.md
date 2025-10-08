# GCP Coffee Sales Pipeline

This project implements a data pipeline for coffee sales analytics using PySpark, Google Cloud Storage (GCS), and BigQuery. It includes data transformation, validation, orchestration with Airflow, and optional visualization.

## Architecture

```
Raw CSV (Bronze) → PySpark Transform (Silver/Gold) → Upload to GCS → Load to BigQuery → Validate → Visualize
```

- **Bronze**: Raw CSV files.
- **Silver**: Cleaned and transformed data (Parquet).
- **Gold**: Aggregated data (Parquet).
- **GCS**: Cloud storage for processed files.
- **BigQuery**: Data warehouse for analytics.
- **Airflow**: Orchestration and scheduling.
- **CI/CD**: Automated validation with GitHub Actions.

## Project Structure

- `src/transform.py` — Cleans and transforms raw sales data using PySpark.
- `src/upload_gcs.py` — Uploads processed files to Google Cloud Storage.
- `src/load_bq.py` — Loads data from GCS into BigQuery tables.
- `tests/data_validation.py` — Validates data quality using Great Expectations.
- `.github/workflows/ci.yml` — GitHub Actions workflow for CI/CD.
- `data/bronze` — Raw data.
- `data/silver` — Cleaned data.
- `data/gold` — Aggregated data.

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repo-url>
   cd gcp-pipeline
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux/Mac:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure GCP credentials**
   - Place your GCP service account key (e.g., `gcp_key.json`) in the project root.
   - Set environment variables as needed for authentication.

## Execution Steps

1. **Activate virtual environment**
   ```bash
   source venv/bin/activate
   ```

2. **Run PySpark transformation**
   ```bash
   python src/transform.py
   ```

3. **Upload files to GCS**
   ```bash
   python src/upload_gcs.py
   ```

4. **Load to BigQuery**
   ```bash
   python src/load_bq.py
   ```

5. **Validate data**
   ```bash
   python tests/data_validation.py
   ```

6. **Schedule DAG with Airflow**
   ```bash
   airflow dags list
   airflow dags trigger gcp_pipeline
   ```

## Sample BigQuery Queries

- **Total sales by coffee type**
  ```sql
  SELECT coffee_name, SUM(total_sales) AS total_sales
  FROM `pipeline_dataset.Coffe_sales_agg`
  GROUP BY coffee_name
  ORDER BY total_sales DESC
  ```

- **Top 10 coffee sales**
  ```sql
  SELECT coffee_name, total_sales
  FROM `pipeline_dataset.Coffe_sales_agg`
  ORDER BY total_sales DESC
  LIMIT 10
  ```

- **Sales by weekday**
  ```sql
  SELECT Weekday, SUM(total_sales) AS sales
  FROM `pipeline_dataset.Coffe_sales_agg`
  GROUP BY Weekday
  ORDER BY sales DESC
  ```

## Optional: Visualization

- Connect Power BI or Google Data Studio to BigQuery (`pipeline_dataset.Coffe_sales_agg`).
- Create KPIs such as revenue by coffee type, top 10 coffees, sales by weekday, etc.

## Optional: CI/CD

- Automated data validation with GitHub Actions on every push or pull request.

---

**Note:**  
Configure your GCP credentials and environment variables as needed.  
See individual scripts for more details.