import psycopg2, config, time
from matplotlib import pyplot as plt

table = "COVID"
num_rows = 100
x = []
y = []

conn = psycopg2.connect(database=config.name, user=config.user, password=config.pswd, host=config.host, port=config.port)
cur = conn.cursor() 

sql = "select * from " + table + ";"
cur.execute(sql)

for i in range(100000//num_rows):
    t1 = time.time()
    rows = cur.fetchmany(num_rows)
    t2 = time.time()
    t = t2-t1
    if t > 0 or True:
        x += [i+1]
        y += [t]

bin = 40
x = [sum(x[i:i+bin])/bin for i in range(0,len(x),bin)]
y = [sum(y[i:i+bin])/bin for i in range(0,len(y),bin)]

cur.close()
conn.close()
plt.plot(x,y)
plt.xlabel("iteration")
plt.ylabel("time (s)")
plt.show()