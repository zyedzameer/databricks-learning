"""
Global Spark Configuration and Session Management.

This module creates and exposes a single SparkSession instance that is reused
across all problem modules, avoiding repeated initialization overhead.

Usage:
    from spark_config import spark
    df = spark.read.csv("data/myfile.csv", header=True, inferSchema=True)
"""

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PySpark Learning") \
    .master("local[*]") \
    .config("spark.driver.host", "127.0.0.1") \
    .config("spark.sql.adaptive.enabled", "true") \
    .getOrCreate()

