# AWWARDS

## Description
This is a website where users can post pictures of their website and its details along with the live link,users can also vote or rate upon it.

## Author 
Owino Lawrence Odhiambo

## User Story 
1. Click on icon to sign in or Register
2. Upload a project with some of its screen shots.
3. Update profile
4. View Api Endpoint
5. Search for different projects using projects title.
6. Hover over image to vote or view project posted

## Setup and Installation
To get the project

Clone this repo {https://github.com/owinolawrence/awwards.git}

### Navigate into the folder and install requirements
cd The-Gram pip install -r requirements.txt 
### Install and activate Virtual
- python3 -m venv virtual - source virtual/bin/activate  
### Install Dependencies
pip install -r requirements.txt 
### Setup Database
SetUp your database User,Password, Host then make migrate

python manage.py makemigrations Awards
### Now Migrate

python manage.py migrate 
### Run the application
python manage.py runserver 
Running the application
python manage.py server 
### Testing the application
python manage.py test 
Open the application on your browser 127.0.0.1:8000.