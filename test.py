import csv
import sqlite3
import os

# direktori tempat file-file SQLite berada
dir_path = '/opt/wazuh-docker/multi-node/data/system-inventory/db/'

# looping untuk mengonversi setiap file SQLite ke file CSV
for file_name in os.listdir(dir_path):
    if file_name.endswith('.db'):
        # membuat koneksi ke database
        conn = sqlite3.connect(os.path.join(dir_path, file_name))
        cursor = conn.cursor()

        # mendapatkan daftar tabel
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        # looping untuk mengonversi setiap tabel ke CSV
        for table_name in tables:
            table_name = table_name[0]

            # mengambil data dari tabel
            cursor.execute(f"SELECT * FROM \"{table_name}\";")
            rows = cursor.fetchall()

            # menulis data ke file CSV
            with open(f"{file_name}_{table_name}.csv", 'w', newline='') as csv_file: 
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([i[0] for i in cursor.description]) 
                csv_writer.writerows(rows)

        # menutup koneksi
        conn.close()
