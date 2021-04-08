from pyspark.sql import SQLContext
from pyspark import SparkContext

if __name__ == "__main__":
    # create Spark context with necessary configuration
    spark = SparkContext("local", "Stock Returns")

    # read csv data from the stock_prices file
    df = SQLContext(spark).read.option("header", True).csv("stock_prices.csv")

    # calculate daily percentage returns
    df = df.withColumn("return", ((df["close"]-df["open"])/df["open"])*100)

    # average on date
    df = df.groupBy("date").avg().alias("avg_return")

    # save the average returns to output
    df.write.csv('./stockreturns/')
