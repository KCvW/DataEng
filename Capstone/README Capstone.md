# Capstone Project - Udacity Data Engineering Nanodegree

## Project Goal

The key milestone of the project is to create a data warehouse that can be used for a broader range of analysis. Coming from this comprehensive data structure the aim is to provide a data basis focusing on immigartion and demographic data sets.

The objective of this project is to create an ETL pipeline for I94 immigration, global land temperatures and US demographics datasets to form an analytics database on immigration events. Typical questions are referring to these data sets.

To fulfill this analytical approach the following steps are necessary:

* Define the scope of the project
* Collect the relevant data
* Explore the data for a deeper understanding
* Ensure the access to the data
* Align on a reliable data model
* Run the ETL process to structure the data
* Completion of project parameters

___

## Define the scope and collect the data

### Scope of the project

This capstone project will focus on three major datasets which will be used to create a data warehouse including respective fact and dimension tables.

* Used Datasets

    1. [US Cities: Demographics](https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/)
    2. [Climate Change: Earth Surface Temperature Data](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data)
    3. [I94 Immigration Data](https://travel.trade.gov/research/reports/i94/historical/2016.html)

* Tools to analyze the data

    1. Python: as programming language - especially to process the data
    2. PySpark: used for large datasets to process the data
    3. Pandas: data analysis for small data sets
    4. AWS S3: used for plain data storage
    5. AWS Redshift: used for data warehousing and data analysis

### Collect the relevant data

The follwoing data sets are recommended and given to fulfil the project goal:

| Data Set | Format / Data Type | Description |
| ---      | ---                | ---         |
| [US Cities: Demographics](https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/) | CSV (Comma Separated Value) | This dataset contains information about the demographics of all US cities and census-designated places with a population greater or equal to 65,000. This data comes from the US Census Bureau's 2015 American Community Survey. |
| [Climate Change: Earth Surface Temperature Data](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data) | CSV (Comma Separated Value) | Provided by Kaggle, this data set points out the average temperature of significant cities and metropoles all over the world. |
| [I94 Immigration Data](https://travel.trade.gov/research/reports/i94/historical/2016.html) | SAS (Statistical Analysis Software) | The US Immigration Center provides information about the arrivals of international travelers focussing on different global regions and countries. Furthermore, it shows data about the visa type, transportation mode, groups of age, visited states, and the top ports of entry. |

___

## Explore & access the datasets

The following steps are necessary to explore and clean the data.

### Explore the datasets

1. To provide an overview of the datasets Pandas will be used for an exploratory approach
2. To understand the data in a better way, it will be split into dimensional tables. If needed the attribute name will be changed
3. To test the ETL logic in regards to the SAS datasets PySpark will be used

### Clean the datasets

1. Transformation to Pandas.datetime is needed for: `arrdate` and `depdate`
2. To create the auxiliary dimension tables the description file has to be parsed for: `country_code`, `city_code`, `state_code`, `mode`, and `visa`
3. Transformation of `city` and `state` to upper case - match to `city_code` and `state_code` tables

___

## Definition of the final data model

Referring to the project goals, it is necessary to define two different models.

1. Star Schema
2. Schema for Data Pipleline

### Star Schema

    [Conceptual Model - Star Schema](https://)

### Steps to build the data pipeline

1. All relevant data should be stored in AWS S3 buckets:

* `[Source_S3_Bucket]/immigration/18-83510-I94-Data-2016/*.sas7bdat`
* `[Source_S3_Bucket]/I94_SAS_Labels_Descriptions.SAS`
* `[Source_S3_Bucket]/temperature/GlobalLandTemperaturesByCity.csv`
* `[Source_S3_Bucket]/demography/us-cities-demographics.csv`

2. Clean up all data sets (see description above)
3. Transformation of immigration data (1 fact and 2 dimension tables - partitioned by state)
4. To get auxiliary tables, the label description file has to be parsed
5. Temperature data has to transformed to dimension table
6. Demographic data has to be split into 2 dimension tables
7. Store all tables in AWS S3 buckets

___

## Run ETL process - structure data

To structure the data it is necessary to focus on several steps which are all related to the ETL process.

### Create the data model

All steps are mention in [xyz.ipynb](https://)

### Check the data quality

These checks include:

* After running the ETL process none of the tables should be blank
* The data schema of each dimensional tables should fit to the data model

For further information please refer to [Check Data Quality.ipynb](https://)

### Data structure

The following images provide an overview of the data structure:
[Data Structure & Model](https://)

___

## Completion of project parameters

This section lists all relevant parameters which are used to fulfil the project goals.

### Technology

* Data Storage - `AWS S3 Buckets`
* Data Analysis (sample data sets) - `Pandas`
* Propcessing large data sets (staging to dimension table) - `PySpark`

### Update Frequency of the Data

* `Immigration` and `Temperature` data tables should be updated on a *montly basis* - the raw data sets are created on a monthly basis as well
* `Demographic` data has an *yearly update frequency* - as these sets are complex and costly to create
* An *append-only mode* for the updates is sufficient

### Design Patterns & Improvements

* All data will be loaded and presented in dedicated dashboards - so the update frequency of the data should be on daily basis (e.g. 06:00am).
  * To schedule a regular update cycle (ETL Pipeline) and to create a status report `Apache Airflow` can be used for automatisation reasons
* More than 100++ users need access to the data base in a concurrent way
  * The data can be moved to `AWS Redshift` as the amount of connections can be handled with more accuracy. As this solution is located in the cloud, a cost/benefit calculation is recommended.
* Data increase factor is close to 100
  * In a stand alone server setup `Spark` cannot handle such a data set - as the solution is cloud-based `AWS EMR` can be used as a distributed data cluster (large datasets in a cloud environment)

### Potential Improvements

From a project perspective it is essential to focus on these topics:

1. To elaborate on reliable data it is necessary to bascially collect more raw data - the main aim should be to have a complete SSOT database
2. The data sets `Immigration` and `Temperature` differ by up to 3 years in regards to the data basis (2016 vs. 2013) - a comparison from a mathematical/statistical standpoint is difficult
3. The attributes `State` and `City` are missing in the description file, so it is hard to merge the immigration and demography table