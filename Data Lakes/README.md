# Data Engineering > Spark and Data Lakes - Project: Data Lake

Sparkify, the well-known music streaming start up has massively grown in regards to the user base and the song database. Hence, they have the need to migrate all the data, which is hosted in a common data warehouse to dedicated data lakes. All relevant data is structured in JSON files - these files resides in AWS S3 buckets. The JSON files log all the user activities and the metadata on the songs which are streamed via the app. 

## Project Scope

The tasks of the responsible data engineer are:

- building an ETL pipeline that extracts the data from AWS S3
- using Spark to processs the data
- loading back the data into the AWS S3 buckets into a set of dimensional tables
- finding insights in regards to the listening behaviour of the users

## Structure of the project

To fulfill all the project tasks Spark and the data lake structure have to be enabled.

* `etl.py`        - Builds the ETL pipeline
* `dl.cfg`        - Configuration file for the AWS cloud icld. the S3 Buckets

## Configuration of AWS S3

Based on the file `dl.cfg` the bucket endpoint (AWS S3) will be created. The file therefore consits of the personal AWS credentials >>> **Please do not publish the AWS credentials officially**

    
    [AWS]
    AWS_ACCESS_KEY_ID = 'AKIA2U73ADUBJK4xxxxx'
    AWS_SECRET_ACCESS_KEY = 'AbV8d0gumOIPN6XmUJ6l6pRaTwMz/ZSnfznyyyyy'

    [AWS S3]
    SOURCE_S3_BUCKET = `s3a://udactity-dend/log_data`
    DEST_S3_BUCKET = `s3a://udacity-dend/song_data`
    LOG_JSONPATH = `s3a://udacity-dend/log_json_path.json`
    

## ETL pipeline

The pipeline builder is based on the file `etl.py` which contains the following functions

1. `process_song_data`
    - Loads raw data from AWS S3 to Spark and processes the song data to insert into the dimension tables _time_ and _users_ plus into the fact table _songplays_

2. `process_log_data`
    - Loads raw data from AWS S3 to Spark and processes the event log data to insert into the dimension tables _time_ and _users_ plus into the fact table _songplays_

### Running the `etl.py`

Install pyspark in the AWS terminal and run the script (Phython file)

    ```
    pip install pyspark
    python3 etl.py
    ```

## Schema of the database

The following fact and dimension tables are used:

### Fact Table

songplays
    songplay_id    INT,
    start_time      TIMESTAMP,
    user_id         INT,
    level           VARCHAR,
    song_id         VARCHAR,
    artist_id       VARCHAR,
    session_id      INT,
    location        TEXT,
    user_agent      Text


### Dimension Tables

users
    user_id         INT,
    first_name      VARCHAR,
    last_name       VARCHAR,
    gender          CHAR(1),
    level           VARCHAR

songs
    song_id         VARCHAR,
    title           VARCHAR,
    artist_id       VARCHAR,
    year            INT,
    duration        FLOAT

artists
    artist_id       VARCHAR,
    name            VARCHAR,
    location        TEXT,
    latitude        FLOAT,
    longitude       FLOAT,

time
    start_time      TIMESTAMP,
    hour            INT,
    day             INT,
    week            INT,
    month           INT,
    year            INT,
    weekday         VARCHAR,