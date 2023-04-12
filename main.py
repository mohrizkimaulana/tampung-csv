import csv
import sqlite3

conn = sqlite3.connect('/opt/wazuh-docker/multi-node/data/system-inventory/db/026.db')
cursor = conn.cursor()
cursor.execute("select * from sys_ports;")
with open("out.csv", 'w',newline='') as csv_file: 
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow([i[0] for i in cursor.description]) 
    csv_writer.writerows(cursor)
conn.close()
