from pyspark.sql import *
from logger import Log4J
from utils import load_survey_df


if __name__ == '__main__':

    spark = SparkSession.builder \
        .appName("HelloSpark") \
        .master("local[3]") \
        .config("spark.driver.extraJavaOptions", "-Dlog4j.configuration=file:log4j.properties") \
        .getOrCreate()


    # spark.sparkContext.setLogLevel("INFO")

    logger = Log4J(spark)

    logger.info("Starting HelloSpark")

    # # processing code
    # survey_df = load_survey_df(spark, "data/sample.csv")
    # survey_df.show()

    logger.info("Finished HelloSpark")

    spark.stop()

