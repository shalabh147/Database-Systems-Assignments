from pyspark.sql import SQLContext
from pyspark import SparkContext
# other required imports here
import re, requests
from operator import add

def crawl(url):
    # skip downloading if not html
    if url[-4:] != "html":
        return []
    s = requests.get("http://hari1500.github.io/CS387-lab7-crawler-website/"+url).text
    rx = r'<a href="[^"]*">'
    # filter only local URLs (remove those starting with http)
    return list(filter(lambda x: x[:4]!="http", [s[x.start()+9:x.end()-2] for x in re.finditer(rx, s)]))

if __name__ == "__main__":
    # create Spark context with necessary configuration
    spark = SparkContext("local", "Web Crawler")

    # create RDD with starting website
    start_url = "1.html"
    rdd = spark.parallelize([start_url])
    new = rdd

    # break if no new URL
    while new.count() > 0:
        new = new.flatMap(crawl).subtract(rdd)
        rdd = rdd.union(new)

    # count the indegree of each URL
    rdd = rdd.map(lambda x: ("/"+x, 1)).reduceByKey(add)

    # save the indegree to output
    rdd.saveAsTextFile("./webcrawler/")
