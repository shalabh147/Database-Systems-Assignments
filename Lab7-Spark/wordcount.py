from pyspark.sql import SQLContext
from pyspark import SparkContext
# other required imports here
import re
from operator import add

def process(line):
    # convert all characters into lower case
    # replace all non-alphanumerics with whitespace
    # split on whitespaces
    # return list of words
    return [line[0][:7]+" "+x for x in re.sub(r'[^0-9a-z]+', ' ', line[1].lower()).split() if x != ""]

if __name__ == "__main__":
    # create Spark context with necessary configuration
    spark = SparkContext("local", "Word Count")

    # read json data from the newsdata directory
    df = SQLContext(spark).read.option("multiLine", True).option("mode", "PERMISSIVE").json("./newsdata")

    # split each line into words
    lines = df.select("date_published", "article_body").rdd
    words = lines.flatMap(process)

    # count the occurrence of each word
    wordCounts = words.map(lambda x: (x, 1)).reduceByKey(add)

    # save the counts to output
    wordCounts.saveAsTextFile("./wordcount/")
