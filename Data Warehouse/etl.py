import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries

def load_staging_tables(cur, conn):
    """
    Loading all files that are stored in the AWS S3 bucket into the stagiing tables by referring to the script sql_queries.py
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()

def insert_tables(cur, conn):
    """
    Selecting and transforming the data from staging into dimensional tables by using the script sql_queries.py
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    """
    Reading the metadata and the user activities from the AWS S3 bucket, transforming the data based on the staginig tables and loading the data into the dimension tables for analysis purposes
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()