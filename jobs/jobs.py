from django.conf import settings
from time import time
import requests
import json
import random
from datetime import datetime

timeZone = datetime.now()

def schedule_api():
    print("설정한 시간에 실행됩니다")
    