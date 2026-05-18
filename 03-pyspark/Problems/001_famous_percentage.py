"""
Question: A table named "famous" has two columns called user_id and follower_id.
It represents each user ID has a particular follower ID. These follower IDs are
also users of hashtag #Facebook / #Meta. Then, find the famous percentage of each user.

Famous Percentage = number of followers a user has / total number of users on the platform

Dataset: famous.csv located in data/ folder with columns (user_id, follower_id)
"""

from pyspark.sql import functions as F
from spark_config import spark

famous_df = spark.read.csv("data/famous.csv", header=True, inferSchema=True)

print("Input `famous` table:")
famous_df.show(truncate=False)

total_users = (
    famous_df
    .select(F.col("user_id").alias("id"))
    .union(famous_df.select(F.col("follower_id").alias("id")))
    .distinct()
    .count()
)

follower_count_df = (
    famous_df.groupBy("user_id").agg(F.count("follower_id").alias("follower_count"))
)

famous_percentage_df = follower_count_df.withColumn(
    "famous_percentage",
    F.round(F.col("follower_count") / F.lit(float(total_users)) * 100, 2)
)

print(f"\nTotal unique users on the platform: {total_users}")
print("\nFamous percentage per user (sorted by user_id):")
famous_percentage_df.orderBy("user_id").show(truncate=False)



