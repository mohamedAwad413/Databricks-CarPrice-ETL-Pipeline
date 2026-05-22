# Databricks notebook source
raw_cars_df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("/Volumes/main/default/my_data_volume/car_price_dataset.csv")

# COMMAND ----------

raw_cars_df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("main.default.bronze_cars")


print("Success read data in bronze layer.")

# COMMAND ----------

bronze_df = spark.read.table("main.default.bronze_cars")
display(bronze_df)