#Transform Data
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, concat_ws, to_timestamp
import pandas as pd

spark = SparkSession.builder.appName("PipelineTransform").getOrCreate()

#read bronze csv data
df = spark.read.csv('../data/bronze/Coffe_sales.csv', header=True, inferSchema=True)

###transformations
#convert columns to appropriate data types
df_clean = df.withColumn("money", col("money").cast("float")) \
    .withColumn("hour_of_day", col("hour_of_day").cast("int")) \
    .withColumn("Weekdaysort", col("Weekdaysort").cast("int")) \
    .withColumn("Monthsort", col("Monthsort").cast("int"))

#Combine Date and Time into a single timestamp column
df_clean = df_clean.withColumn("datetime", to_timestamp(concat_ws(' ', col("Date"), col("Time")), "MM/dd/yyyy HH:mm.ss"))

# Drop rows with nulls in important columns
df_clean = df_clean.dropna(subset=["money", "datetime"])

# Example aggregation: total sales per coffee type
df_agg = df_clean.groupBy("coffee_name").sum("money").withColumnRenamed("sum(money)", "total_sales")

# Save silver and gold
df_clean.write.mode('overwrite').parquet('../data/silver/Coffe_sales.parquet')
df_agg.write.mode('overwrite').parquet('../data/gold/Coffe_sales_agg.parquet')
