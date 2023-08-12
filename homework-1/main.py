"""Скрипт для заполнения данными таблиц в БД Postgres."""
import pathlib

import psycopg2
import csv

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='timur')


def insert_employees():
    filepath = pathlib.Path.cwd() / 'north_data' / 'employees_data.csv'

    try:
        with conn:
            with conn.cursor() as cur:
                with open(filepath, 'r') as file:
                    reader = csv.reader(file)
                    columns = next(reader)
                    query = 'INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s)'
                    for data in reader:
                        cur.execute(query, data)
    finally:
        conn.close()


def insert_customers():
    filepath = pathlib.Path.cwd() / 'north_data' / 'customers_data.csv'
    try:
        with conn:
            with conn.cursor() as cur:
                with open(filepath, 'r') as file:
                    reader = csv.reader(file)
                    columns = next(reader)
                    query = 'INSERT INTO customers VALUES(%s, %s, %s)'
                    for data in reader:
                        cur.execute(query, data)
    finally:
        conn.close()


def insert_orders():
    filepath = pathlib.Path.cwd() / 'north_data' / 'orders_data.csv'
    try:
        with conn:
            with conn.cursor() as cur:
                with open(filepath, 'r') as file:
                    reader = csv.reader(file)
                    columns = next(reader)
                    query = 'INSERT INTO orders VALUES(%s, %s, %s, %s, %s)'
                    for data in reader:
                        cur.execute(query, data)
    finally:
        conn.close()


# insert_employees()
# insert_customers()
# insert_orders()
