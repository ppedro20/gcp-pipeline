#Data validation
import great_expectations as ge
import pandas as pd

df = pd.read_parquet('../data/gold/Coffe_sales_agg.parquet')
gdf = ge.from_pandas(df)

# Expect no nulls
gdf.expect_column_values_to_not_be_null("coffee_name")
gdf.expect_column_values_to_not_be_null("total_sales")

# Expect correct data types
gdf.expect_column_values_to_be_of_type("coffee_name", "object")
gdf.expect_column_values_to_be_of_type("total_sales", "float64")

# Expect non-negative sales
gdf.expect_column_values_to_be_between("total_sales", min_value=0)

# Expect unique coffee names
gdf.expect_column_values_to_be_unique("coffee_name")

# Expect at least one row
gdf.expect_table_row_count_to_be_between(min_value=1)
