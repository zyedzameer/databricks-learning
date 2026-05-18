"""
Question: Given a table `sf_transactions` of purchases by date, calculate the month-over-month
percentage change in revenue. The output should include the year-month date (YYYY-MM)
and percentage change, rounded to the 2nd decimal point, and sorted from the beginning
of the year to the end of the year. The percentage change column will be populated
from the 2nd month forward and calculated as ((this month's revenue — last month's revenue) / last month's revenue)*100.

Dataset: sf_transactions.csv located in data/ folder with columns (id, created_at, value, purchase_id)

Approach:
1. Create year_month column from created_at using date_format
2. Aggregate total revenue per month
3. Use window function LAG to get previous month's revenue
4. Calculate percentage change and round to 2 decimals
5. First month will have null percentage change
"""

from pyspark.sql import functions as F
from pyspark.sql.window import Window
from spark_config import spark

sf_df = spark.read.csv("data/sf_transactions.csv", header=True, inferSchema=True)

print("Input `sf_transactions` table:")
sf_df.show(5, truncate=False)

monthly_revenue = (
    sf_df
    .withColumn("year_month", F.date_format(F.col("created_at"), "yyyy-MM"))
    .groupBy("year_month")
    .agg(F.sum(F.col("value")).alias("total_revenue"))
    .orderBy("year_month")
)

w = Window.orderBy("year_month")
with_prev = monthly_revenue.withColumn("previous_revenue", F.lag("total_revenue").over(w))

result = with_prev.withColumn(
    "pct_change",
    F.when(
        F.col("previous_revenue").isNull(),
        None,
    ).otherwise(
        F.round(
            (F.col("total_revenue") - F.col("previous_revenue")) / F.col("previous_revenue") * 100,
            2
        )
    ),
).select("year_month", "total_revenue", "previous_revenue", "pct_change")

print("\nMonth-over-month revenue change (chronological order):")
result.show(truncate=False)

