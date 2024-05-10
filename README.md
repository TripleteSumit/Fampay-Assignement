# 🙌Fampay Assignement 🙌

## About the Project

It's a simple video listing application fetch from youtube apis and show it to custom apis

## Start Project

```bash
    git clone <http link>
```

```bash
    install python and navigate to project folder and
    run the command 'python3 -m venv venv'
```

```bash
    select the virtual env python interpreter by pressing
    ctrl + shift + p
```

```bash
    pip install -r requirements.txt
```

```bash
    Execute below command one by one or by using '&&' operator
    1. sudo apt install redis-server
    2. sudo service redis-server status #check for activeness
    3. sudo apt install mysql-server
    4. mysql --version #check  weather it is install correctly or not
    5. mysql -u <user_name> -p <enter password>
    6. CREATE DATABASE food_db;
    7. SHOW DATABASES;
    8. python manage.py makemigrations
    9. python manage.py migrate
    10. sudo service mysql start
    11. sudo service redis start
    # use status to check the activeness
    12. python manage.py runserver
    # open another terminal run
    13. celery -A home beat --loglevel=info #to see the log
    # open another terminal run
    14. celery -A home worker --loglevel=info
```

## Limitation

use linux system as celery configuring doesn't support in windows

## Result

- After configuring the project when you hit the get api you can get the latest videos in chronological order
- Youtube API get call in every 10 second if the quota limit is finished then it jump to another API_KEY (only two api keys used here)

## Test the API

- [POSTMAN](https://github.com/TripleteSumit/Fampay-Assignement/blob/master/Fampay.postman_collection.json)
