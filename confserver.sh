#!/bin/bash
sudo apt-get install python
sudo apt-get update
sudo apt-get upgrade
sudo apt install python-pip
sudo apt-get install python-dev build-essential
sudo pip install virtualenv virtualenvwrapper
pip install Flask
sudo apt install python3-flask
sudo apt-get install git-core
git clone git://github.com/IgnatiusPunset/server
export FLASK_APP=server.py 
flask run --host=0.0.0.0
