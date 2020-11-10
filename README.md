# Online-monitoring Django Application

Django web application that allows you to view the statistics of the exchange site in real time

## How to use

For the app to work, you need to install Docker
https://docs.docker.com/engine/install/ubuntu/

Then сlone this repository and go to the project directory

    git clone https://github.com/prosto-kosmos/online_monitoring
    cd online_monitoring/

Install the venv library if it is not installed

    sudo apt install python3-venv

Install and activate the environment variable

    python3 -m venv venv
    source venv/bin/activate

Install all the necessary project requirements

    pip install -r requirements.txt

Go to the application folder, perform migrations, and start the server

    cd grath/
    python manage.py migrate
    python manage.py runserver

Open a new terminal in the root directory of the project. Then activate the environment variable and launch the container with redis

    source venv/bin/activate
    sudo docker run -d -p 6379:6379 redis
    
Go to the folder with the app and launch the worker

    cd grath/
    celery -A grath worker -l info
