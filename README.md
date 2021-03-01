# Online-monitoring Django Application

Django web application that allows you to view the statistics of the exchange site in real time

## How to use

Then сlone this repository and go to the project directory

    git clone https://github.com/prosto-kosmos/Online_monitoring
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
    python manage.py runserver --insecure

Open `127.0.0.1:8000` in a browser
