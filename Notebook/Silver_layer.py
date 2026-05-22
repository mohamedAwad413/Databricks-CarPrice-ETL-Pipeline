# Databricks notebook source
from pyspark.sql.functions import current_timestamp


bronze_df = spark.read.table("main.default.bronze_cars")


cleaned_df = bronze_df.dropDuplicates() \
                      .withColumn("ingestion_time", current_timestamp())


cleaned_df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("main.default.silver_cars")

print("Done Success Cleaned in silver layer.")

display(bronze_df)