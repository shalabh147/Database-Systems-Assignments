import psycopg2, config, time

table = "COVID"
csv_files = ["data1.csv","data2.csv","data3.csv","data4.csv","data5.csv"]

for file in csv_files:
    conn = psycopg2.connect(database=config.name, user=config.user, password=config.pswd, host=config.host, port=config.port)
    cur = conn.cursor()
    sql = "delete from " + table + ";"
    cur.execute(sql)
    cur.close()
    conn.commit()
    conn.close()
    t1 = time.time()
    conn = psycopg2.connect(database=config.name, user=config.user, password=config.pswd, host=config.host, port=config.port)
    cur = conn.cursor()
    sql = "copy " + table + " from STDIN csv header;"
    f = open(file, "r")
    cur.copy_expert(sql, f)
    cur.close()
    conn.commit()
    conn.close()
    t2 = time.time()
    print(file, " ", t2-t1)