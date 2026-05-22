# Databricks notebook source
from pyspark.sql.functions import avg, round, count


silver_df = spark.read.table("main.default.silver_cars")

gold_df = silver_df.groupBy("Brand") \
                    .agg(
                        round(avg("Price"), 2).alias("Average_Price"),
                        count("Car_ID").alias("Total_Cars_Count")
                    )

gold_df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("main.default.gold_cars_analysis")

print("Done! Gold layer table created successfully.")

display(gold_df)