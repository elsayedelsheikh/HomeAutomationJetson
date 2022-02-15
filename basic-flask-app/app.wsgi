#!/usr/bin/python3
import sys
sys.path.insert(0,"/var/www/basic-flask-app")

#activate_this ='/home/sayed/.local/share/virtualenvs/basic-flask-app-2sD0MLz9/bin/activate_this.py'
#with open(activate_this) as file_:
#	exect(file_.read(), dict(__file__=activate_this))

from app import app as application

