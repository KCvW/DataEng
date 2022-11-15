# Data Enginieering > Data Modeling - Project: Data Modeling with Postgres

The initial position of the project is a startup called Sparkify which acts a music streaming app. 
Coming from a customer journey the analytics team is interesed to get a deeper understanding of the usage of the app, espacially in regards to songs that are played by the users.

Adapted from JSON files they have a directory which is analyzed in a highly manual way. So the team is keen to have an automated solution to optimize teh queries and to act on reliable results.

## Project Scope

As a data engineer the main tasks are:

- create a Postgres database schema
- based on this database to optimize queries
- establish an ETL pipeline
- test the database and the ETL pipeline
- evaluatze the results

## Description of Database Schema

The database schema consitst of a fact table **songsplay** and four dimension tables **users, songs, artists and time**.
This is the structure of the tables:

### Fact Table

songsplay
	- songplay_id PRIMARY KEY
	- start_time REFERENCES time (start_time)
	- user_id REFERENCES users (user_id)
	- level
	- song_id REFERENCES songs (song_id)
	- artist_id REFERENCES artists (artist_id)
	- session_id
	- location
	- user_agent
	
### Dimension Tables

users
	- user_id PRIMARY KEY
	- first_name
	- last_name
	- gender
	- level
	
songs
	- song_id PRIMARY KEY
	- title
	- artist_id
	- year
	- duration
	
artists
	- artist_id PRIMARY KEY
	- artist_name
	- artist_location
	- artist_latitude
	- artist_longitude
	
time
	- start_time
	- hour
	- day
	- week
	- month
	- year
	- weekday


## ETL Pipeline creation

The pipeline consists of three files written in **Python**. There are the pipeline builder, the creation process for the fact and dimension tables, and the helper for the SQL queries.

### File: etl.py

This is the pipeline builder itself that is based on:
	1. process_data **iterating the datasets**
	2. process_song_files **inserts data into the dimension tables**
	3. process_log_file **Processes the logfile**

### File: create_tables.py

Used for the creation of the fact and dimension tables
	1. create_database
	2. drop_tables
	3. create_tables
	
### File: sql_queries.py

Helper statements for the above mentioned files
	1. table_drop
	2. table_create
	3. table_insert
	4. song_select