import csv

file = open("loaddata.cypher", 'w')

with open("users.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        file.write('CREATE (:User {id: ' + row[0] + ', name: "' + row[1] + '"});\n')

with open("tweets.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        file.write('CREATE (:Tweet {id: ' + row[0] + ', text: "' + row[1] + '"});\n')

with open("hashtags.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        file.write('CREATE (:Hashtag {id: ' + row[0] + ', tag: "' + row[1] + '"});\n')

with open("follows.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        file.write('MATCH (a:User {id: ' + row[0] + '}), (b:User {id: ' + row[1] + '}) CREATE (a)-[:Follows]->(b);\n')

with open("sent.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        file.write('MATCH (a:User {id: ' + row[0] + '}), (b:Tweet {id: ' + row[1] + '}) CREATE (a)-[:Sent]->(b);\n')

with open("mentions.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        file.write('MATCH (a:Tweet {id: ' + row[0] + '}), (b:User {id: ' + row[1] + '}) CREATE (a)-[:Mentions]->(b);\n')

with open("contains.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        file.write('MATCH (a:Tweet {id: ' + row[0] + '}), (b:Hashtag {id: ' + row[1] + '}) CREATE (a)-[:Contains]->(b);\n')