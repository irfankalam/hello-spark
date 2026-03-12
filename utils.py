from pyspark.sql import DataFrame
from pyspark.sql.connect.session import SparkSession


def load_survey_df(spark: SparkSession, file_path: str) -> DataFrame:
    return spark.read \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .csv(file_path)