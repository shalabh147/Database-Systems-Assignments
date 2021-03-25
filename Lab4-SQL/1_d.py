import psycopg2, config, csv, time

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
    
    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)

        for row in csvreader:
            sql = "insert into " + table + " values ("
            n = len(row)
            for i in range(n):
                sql += "'" + row[i] + "'"
                if i < n-1:
                    sql += ", "
            sql += ");"
            cur.execute(sql)

    cur.close()
    conn.commit()
    conn.close()
    t2 = time.time()
    print(file, " ", t2-t1)