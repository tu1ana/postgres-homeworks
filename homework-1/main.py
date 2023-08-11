"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='timur')


def insert_employees():

    try:
        with conn:
            with conn.cursor() as cur:
                with open("C:\\Users\\MSI\\PycharmProjects\\postgres-homeworks\\homework-1\\north_data\\employees_data.csv", 'r') as file:
                    reader = csv.reader(file)
                    columns = next(reader)
                    query = 'INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s)'
                    for data in reader:
                        cur.execute(query, data)
    finally:
        conn.close()


def insert_customers():
    try:
        with conn:
            with conn.cursor() as cur:
                with open("C:\\Users\\MSI\\PycharmProjects\\postgres-homeworks\\homework-1\\north_data\\customers_data.csv", 'r') as file:
                    reader = csv.reader(file)
                    columns = next(reader)
                    query = 'INSERT INTO customers VALUES(%s, %s, %s)'
                    for data in reader:
                        cur.execute(query, data)
    finally:
        conn.close()


def insert_orders():
    try:
        with conn:
            with conn.cursor() as cur:
                with open("C:\\Users\\MSI\\PycharmProjects\\postgres-homeworks\\homework-1\\north_data\\orders_data.csv", 'r') as file:
                    reader = csv.reader(file)
                    columns = next(reader)
                    query = 'INSERT INTO orders VALUES(%s, %s, %s, %s, %s)'
                    for data in reader:
                        cur.execute(query, data)
    finally:
        conn.close()


# insert_employees()
# insert_customers()
insert_orders()

# try:
#     with conn:
#         with conn.cursor() as cur:
#             with open("C:\\Users\\MSI\\PycharmProjects\\postgres-homeworks\\homework-1\\north_data\\employees_data.csv", 'r') as file, \
#                  open("C:\\Users\\MSI\\PycharmProjects\\postgres-homeworks\\homework-1\\north_data\\customers_data.csv", 'r') as file_1, \
#                  open("C:\\Users\\MSI\\PycharmProjects\\postgres-homeworks\\homework-1\\north_data\\orders_data.csv", 'r') as file_2:
#                 reader = csv.reader(file)
#                 reader_1 = csv.reader(file_1)
#                 reader_2 = csv.reader(file_2)
#                 columns = next(reader)
#                 columns_1 = next(reader_1)
#                 columns_2 = next(reader_2)
#                 query = 'INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s)'
#                 query_1 = 'INSERT INTO customers VALUES(%s, %s, %s)'
#                 query_2 = 'INSERT INTO orders VALUES(%s, %s, %s, %s, %s)'
#                 cursor = conn.cursor()
#                 cursor_1 = conn.cursor()
#                 cursor_2 = conn.cursor()
#                 for data in reader:
#                     cursor.execute(query, data)
#
#                 for data in reader_1:
#                     cursor_1.execute(query_1, data)
#
#                 for data in reader_2:
#                     cursor_2.execute(query_2, data)
# finally:
#     conn.close()
