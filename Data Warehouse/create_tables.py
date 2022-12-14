import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
    Deletion of existing tables so that new ones can be created initially
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

def create_tables(cur, conn):
    """
    Creation of staging and dimension tables based on the script sql_queries.py
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def main():
    """
    Initializing the database and creation of the required tables - reading of the configuration file dhw.cfg
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()