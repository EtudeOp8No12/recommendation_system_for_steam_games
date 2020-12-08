# Recommendation System for Steam Games

1. [Installation and Access Setup](#installation)
2. [Project Motivation](#motivation)
3. [Data Collection](#data)
4. [File Descriptions](#files)
5. [Future Work](#work)

## Installation and Access Setup <a name="installation"></a>
This project utilizes the following packages and services:
- Python 3.0
- Spark/PySpark
- MySQL 

In addition, the following libraries/packages are required:
- bs4
- json
- numpy
- pandas 
- pyspark
- requests
- sklearn
- threading
- time
- tqdm
- sqlalchemy
- yaml

You also need to have [Steam developer account](https://partner.steamgames.com/) to access their API.


## Project Motivation <a name="motivation"></a>
This project aims to prototype and compare recommendation systems for Steam games based on the following types of algorithms:
- popularity-based
- content-based
- item-to-item collaborative filtering
- matrix factorization

## Data Collection <a name="data"></a>
- Steam User ID: scraped ~5,000 steam user IDs from a [third party gaming website](https://wiki.teamfortress.com/wiki/Template:Dictionary/steam_ids/id_list) and utilized Steam API.
- Steam Games Details: obtained using Steam API
- Games owned by Steam users and users' play time: obtained using Steam API

Data will not be published in this repo in case it is against Steam's policy. 

## File Descriptions <a name="files"></a>

- '1_get_user_id.py', '2_get_app_details.py', and '3_get_owned_games.py' include functions to collect the user IDs, games owned by the users, user’s playtime, and details of the games using web scraping and Steam’s API. Data obtained will also be saved into MySQL database to be used for the recommendation system
- '4_recommendation.py' prototypes popularity-based and content-based recommendation systems as well as collaborative filtering with item-based approach and matrix factorization approach (by applying the alternating least square algorithm). Spark framework is used to scale the recommendation systems.

## Future Work <a name="work"></a>
A web app will be built upon those recommendation systems with user interface to demonstrate the performance of each type of recommendation system. 