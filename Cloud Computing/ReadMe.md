# Data Enginieering > Data Warehouse - Project: Cloud Data Warehousing

The cornerstone of the project is a startup called Sparkify, a start up which is streaming music to its customers. Coming from a sophisticated song database the company likes to move their entire processes and the respective data onto a professional cloud solution. Key facts are the useage of a AWS S3 data bucket in connection with JSON based log files. The JSON files are triggerinig the user's activities on the app plus the metadata of the songs. 

## Project scope

As a data engineer the main tasks are:

- building an ETL pipeline that extracts their data from S3
- staging the data in AWS Redshift
- transforming the data into a set of dimensional tables for analytical reasons
- finding insights to what kind of songs the customers are listening to

## ETL Pipeline

The ETL pipeline consists of three Python file which are described below.

### etl.py

The primary file ist the the ETL pipeline builder

1. `load_staging_tables`
    loading the raw data from the AWS S3 Bucket into the staging tables hosted in Redshift
2. `insert_tables`
    transformation process of the staging tables to dimensiojnal tables - needed to do the analytics

### create_tables.py

Focusing in the schema to create staging, fact, and dimension tables

1. `drop_tables`
2. `create_tables`

### sql_queries.py

Collection of certain SQL query statements for the before-mentioned files: 'create_tables' and 'etl.py'

1. `*_table_drop`
2. `*_table_create`
3. `staging_*_copy`
4. `*_table_insert`

## Database Schema

The database schema consists of staging tables, a fact table and multiple dimension tables. IN detail the structure is as follows:

### Staging Tables

staging_events
    artist VARCHAR,
    auth VARCHAR,
    firstName VARCHAR,
    gender CHAR(1),
    itemInSession INT,
    lastName VARCHAR,
    length FLOAT,
    level VARCHAR,
    location TEXT,
    method VARCHAR,
    page VARCHAR,
    registration VARCHAR,
    sessionId INT,
    song VARCHAR,
    status INT,
    ts BIGINT,
    userAgent TEXT,
    userId INT

staging_songs
    artist_id VARCHAR,
    artist_latitude FLOAT,
    artist_location TEXT,
    artist_longitude FLOAT,
    artist_name VARCHAR,
    duration FLOAT,
    num_songs INT,
    song_id VARCHAR,
    title VARCHAR,
    year INT


### Fact Table

songplays
    songplay_id INT IDENTITY(0,1),
    start_time TIMESTAMP,
    user_id INT,
    level VARCHAR,
    song_id VARCHAR,
    artist_id VARCHAR,
    session_id INT,
    location TEXT,
    user_agent TEXT


### Dimension Tables

users
    user_id INT,
    first_name VARCHAR,
    last_name VARCHAR,
    gender CHAR(1),
    level VARCHAR

songs
    song_id VARCHAR,
    title VARCHAR,
    artist_id VARCHAR,
    year INT,
    duration FLOAT

artists
    artist_id VARCHAR,
    name VARCHAR,
    location TEXT ,
    latitude FLOAT ,
    longitude FLOAT

time
    start_time TIMESTAMP,
    hour INT,
    day INT,
    week INT,
    month INT,
    year INT,
    weekday VARCHAR