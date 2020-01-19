import os
import re
from datetime import timedelta

system_name = os.popen('whoami').readline().strip()

try:
    host = os.popen('hostname').readline()
except:
    host = "zhang"

class Config(object):
    SECRET_KEY = 'Dev'
    PERMANENT_SESSION_LIFETIME = timedelta(days=2)

    # environment variables
    USER_NAME = system_name
    RUN_PATH = os.path.dirname(os.path.realpath(__file__))
