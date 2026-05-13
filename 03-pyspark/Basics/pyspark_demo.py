from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, LongType, StringType

try:
    # Create SparkSession with modern configuration for PySpark 4.1.1
    spark = SparkSession.builder \
        .appName("PySpark Demo") \
        .master("local[*]") \
        .config("spark.driver.host", "127.0.0.1") \
        .config("spark.sql.adaptive.enabled", "true") \
        .getOrCreate()

    # Define schema explicitly (modern best practice for type safety)
    schema = StructType([
        StructField("id", LongType(), True),
        StructField("name", StringType(), True)
    ])

    # Create DataFrame with explicit schema
    data = [(1, "Alice"), (2, "Bob")]
    df = spark.createDataFrame(data, schema=schema)

    # Display schema
    print("Schema:")
    df.printSchema()

    print("\nFramework:")
    print(f"Spark Version: {spark.sparkContext.version}")
    print(f"App Name: {spark.sparkContext.appName}")


finally:
    spark.stop()
