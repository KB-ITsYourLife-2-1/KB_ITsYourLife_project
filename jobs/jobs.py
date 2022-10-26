from django.conf import settings
from time import time
import requests
import json
import random
from datetime import datetime
import subprocess

timeZone = datetime.now()

def schedule_api1():
    subprocess.call(["python", "jobs/crowling.py"])

def schedule_api2():
    subprocess.call(["python", "jobs/graph.py"])

def schedule_api3():
    subprocess.call(["python", "jobs/LSTM.py"])
    