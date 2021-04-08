from pyspark.sql import SQLContext
from pyspark import SparkContext
# other required imports here
import re, requests
from operator import add

def crawl(url):
    url = "https://hari1500.github.io/CS387-lab7-crawler-website/" + url
    # skip downloading if not html
    if "html" not in requests.head(url).headers.get('content-type'):
        return []
    # filter local URLs (remove those starting with http)
    return [x.split('"')[1] for x in re.findall('<a[ ]+href[ ]*=[ ]*"[^{http}].*[{.html}]?">', requests.get(url).text)]

if __name__ == "__main__":
    # create Spark context with necessary configuration
    spark = SparkContext("local", "Web Crawler")

    # create RDD with starting website
    start_url = "1.html"
    rdd = spark.parallelize([start_url])
    new = rdd

    # break if no new URL
    while new.count() > 0:
        new = new.flatMap(crawl)
        old = rdd
        rdd = rdd.union(new)
        new = new.subtract(old).distinct()

    # count the indegree of each URL
    rdd = rdd.map(lambda x: ("/"+x, 1)).reduceByKey(add)

    # save the indegree to output
    rdd.saveAsTextFile("./webcrawler/")
