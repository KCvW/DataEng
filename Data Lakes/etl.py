import configparser
from datetime import datetime
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import expr
from pyspark.sql.functions import year, month, dayofmonth, hour, weekofyear, date_format
from pyspark.sql.functions import monotonically_increasing_id
from pyspark.sql.types import StructType, StructField, DoubleType, StringType

# Reading the config file to create the S3 bucket on AWS
config = configparser.ConfigParser()
config.read('dl.cfg', encoding = 'utf-8-sig')


# Assigning the AWS credentials to initiate the infrastructure in the cloud
os.environ['AWS_ACCESS_KEY_ID']=config['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY']=config['AWS_SECRET_ACCESS_KEY']

def create_spark_session():
    """
    Creating the Spark session
    """
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark

def process_song_data(spark, input_data, output_data):    
    """
    Processing the song data and creating the tables for songs and artists
    """    
    # get filepath to song data file
    song_data = os.path.join(input_data + 'song_data/A/A/A/*.json')
    
    # read song data file
    song_schema = StructType([
            StructField("song_id", StringType(),True),
            StructField("title", StringType(),True),
            StructField("artist_id", StringType(),True),
            StructField("year", DoubleType(),True),
            StructField("duration", StringType(),True)
        ])
    df = spark.read.json(song_data, schema=song_schema)

    # extract columns to create songs table
    songs_table = df.select('song_id', 'title', 'artist_id', 'year', 'duration').dropDuplicates(subset=['song_id'])
    
    # write songs table to parquet files partitioned by year and artist
    songs_table.write.mode("overwrite").partitionBy('year', 'artist_id')\
                .parquet(path=output_data + 'songs')

    # extract columns to create artists table
    artists_table = df.select('artist_id', 'artist_name', 'artist_location',\
                             'artist_latitude', 'artist_longitude').dropDuplicates(subset=['artist_id'])
    
    # write artists table to parquet files
    artists_table.write.mode("overwrite").parquet(path=output_data + 'artists')


def process_log_data(spark, input_data, output_data):
        """
        Processing the log data and creating the tables users, time and songplays
        """   
        # get filepath to log data file
        log_data = os.path.join(input_data + 'log_data/*/*/*.json')

        # read log data file
        log_schema = StructType([
        StructField("userID", StringType(),True),
        StructField("firstName", StringType(),True),
        StructField("lastName", StringType(),True),
        StructField("gender", DoubleType(),True),
        StructField("level", DoubleType(),True)
    ])
        df = spark.read.json(log_data, schema=log_schema)
    
        # filter by actions for song plays
        df = df.where(df['page'] == 'NextSong')

        # extract columns for users table    
        users_table = df.select('userId', 'firstName', 'lastName', 'gender', 'level').dropDuplicates(subset=['userId'])
            
        # write users table to parquet files
        users_table.write.mode("overwrite").parquet(path=output_data + 'users')

        """
                create timestamp column from original timestamp column
                get_timestamp = udf()
                df = 
                
                create datetime column from original timestamp column
                get_datetime = udf()
                df = 
        """
            
        # extract columns to create time table
        df = df.withColumn('start_time', (df['ts']/1000).cast('timestamp'))
        df = df.withColumn('weekday', date_format(df['start_time']))
        df = df.withColumn('year', year(df['start_time']))
        df = df.withColumn('month', month(df['start_time']))
        df = df.withColumn('week', week(df['start_time']))
        df = df.withColumn('day', day(df['start_time']))
        df = df.withColumn('hour', hour(df['start_time']))
        time_table = df.select('start_time', 'weekday', 'year', 'month', 'week', 'day', 'hour')
            
        # write time table to parquet files partitioned by year and month
        time_table.write.mode('overwrite').partitionBy('year', 'month').parquet(path=output_data + 'time') 

        # read in song data to use for songplays table
        song_df = spark.sql("SELECT * FROM song_data_view")

        # extract columns from joined song and log datasets to create songplays table 
        songplays_table = df.join(song_df, (df.song == song_df.title)\
                                    & (df.artist == song_df.artist_name)\
                                    & (df.length == song_df.duration), "inner")\
                            .select('start_time', 'user_id', 'level', 'song_id'\
                                'artist_id', 'sessionId', 'location', 'userAgent',\
                                df['year'].alias('year'), df['month'].alias('month'))\
                            .withColumn("songplay_id", monotonically_increasing_id())

        # write songplays table to parquet files partitioned by year and month
        songplays_table.write.mode("overwrite").partitionBy('year', 'month').parquet(path=output_data + 'songplays')


def main():
    spark = create_spark_session()
    input_data = "s3a://udacity-dend/"
    output_data = "s3a://sparkify-outputs"
    
    process_song_data(spark, input_data, output_data)    
    process_log_data(spark, input_data, output_data)


if __name__ == "__main__":
    main()