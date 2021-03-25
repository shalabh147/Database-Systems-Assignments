import csv

table = "COVID"
csv_files = ["data1.csv","data2.csv","data3.csv","data4.csv","data5.csv"]

for csv_filename in csv_files:
    sql_filename = csv_filename.split('.')[0] + ".sql"
    sql_file = open(sql_filename, "w")
    sql_file.close()
    sql_file = open(sql_filename, "a")
    sql_file.write("begin;\n")
    sql_file.write("delete from " + table + ";\n")

    with open(csv_filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)
        for row in csvreader:
            sql_file.write("insert into " + table + " values (")
            n = len(row)
            for i in range(n):
                if row[i] in ["NULL", ""]:
                    sql_file.write("NULL")
                else:
                    sql_file.write("'" + row[i] + "'")
                if i < n-1:
                    sql_file.write(", ")
            sql_file.write(");\n")

    sql_file.write("end;\n")
    sql_file.close()