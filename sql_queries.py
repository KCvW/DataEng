# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS user"
song_table_drop = "DROP TABLE IF EXISTS songs"
arist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id SERIAL PRIMARY KEY,
        start_time TIMESTAMP REFERENCES time (start_time),
        user_id INT REFERENCES users (user_id),
        level VARCHAR,
        song_id VARCHAR REFERENCES songs (song_id),
        artist_id VARCHAR REFERENCES artists (artist_id),
        session_id INT,
        location TEXT,
        user_agent TEXT
    )
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INT PRIMARY KEY,
        first_name VARCHAR,
        last_name VARCHAR,
        gender CHAR(1)
		level VARCHAR
    )
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id VARCHAR PRIMARY KEY,
		title VARCHAR,
		artist_id VARCHAR REFERENCES artists (artist_id),
		year INT,
		duration FLOAT
    )
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id VARCHAR PRIMARY KEY,
		artist_name VARCHAR,
		artist_location TEXT,
		artist_latitude FLOAT,
		artist_longitude FLOAT					   
    )
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time TIMESTAMP PRIMARY KEY
		hour INT,
		day INT,
		week INT,
		month INT,
		year INT,
		weekday VARCHAR
    )
""")



# INSERT RECORDS

songplay_table_insert = "INSERT INTO songplay
    (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cur.execute(insert_query, data)
    
songplay_table_insert = "INSERT INTO user
    (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)"
    cur.execute(insert_query, data)

songplay_table_insert = "INSERT INTO song
    (song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)"
    cur.execute(insert_query, data)

songplay_table_insert = "INSERT INTO artist
    (artist_id, artist_name, artist_location, artist_latitude, artist_longitude)
    VALUES (%s, %s, %s, %s, %s)"
    cur.execute(insert_query, data)    

songplay_table_insert = "INSERT INTO time
    (start_time, hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cur.execute(insert_query, data)

# FIND SONGS

song_select = ("""
	SELECT songs.song_id, artists.artist.id
	FROM songs JOIN artists ON songs.artist_id = artists.artist_id
	WHERE songs.title=%s AND artists.artist_name=%s AND songs.duration=%s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]