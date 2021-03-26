import csv

file = open("loaddata.cypher", 'w')

user = {}
tweet = {}
hashtag = {}

with open("users.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        user[row[0]] = row[1]
        file.write('CREATE (:User {name: "' + row[1] + '"});\n')

with open("tweets.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        tweet[row[0]] = row[1]
        file.write('CREATE (:Tweet {text: "' + row[1] + '"});\n')

with open("hashtags.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        hashtag[row[0]] = row[1]
        file.write('CREATE (:Hashtag {tag: "' + row[1] + '"});\n')

with open("follows.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        file.write('MATCH (a:User {name: "' + user[row[0]] + '"}), (b:User {name: "' + user[row[1]] + '"}) CREATE (a)-[:Follows]->(b);\n')

with open("sent.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        file.write('MATCH (a:User {name: "' + user[row[0]] + '"}), (b:Tweet {text: "' + tweet[row[1]] + '"}) CREATE (a)-[:Sent]->(b);\n')

with open("mentions.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        file.write('MATCH (a:Tweet {text: "' + tweet[row[0]] + '"}), (b:User {name: "' + user[row[1]] + '"}) CREATE (a)-[:Mentions]->(b);\n')

with open("contains.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        file.write('MATCH (a:Tweet {text: "' + tweet[row[0]] + '"}), (b:Hashtag {tag: "' + hashtag[row[1]] + '"}) CREATE (a)-[:Contains]->(b);\n')