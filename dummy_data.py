import requests
import json
from datetime import datetime,timedelta
import time
from random import randrange,randint

def update_fillingLevel(level, date):
    url = "http://localhost:1026/v2/entities/urn:ngsi-ld:WasteContainer:001/attrs/fillingLevel"

    payload = json.dumps({
    "type": "StructuredValue",
    "value": {
        "type": "Number",
        "value": level,
        "unitCode": "P1"
    },
    "metadata": {
        "TimeInstant": {
        "type": "DateTime",
        "value": date#"2019-08-23T03:00:00.000Z"
        }
    }
    })
    headers = {
    'Content-Type': 'application/json',
    'fiware-service': 'citcom',
    'fiware-servicepath': '/'
    }

    response = requests.request("PUT", url, headers=headers, data=payload)

    print(response.text)


def fill_fake_data():
    initial_date=datetime.strptime("2021-12-31T12:00:00Z", "%Y-%m-%dT%H:%M:%SZ")

    filling_level = 0
    for day in range(365):
        next_date = initial_date+timedelta(hours=24*(day+1))
        #print(x+1)
        #print(next_date.isoformat())
        #update_fillingLevel(next_date.isoformat(),x)
        
        if filling_level > randint(80,98):
            filling_level=randint(0,2)

        filling_level += randrange(6)

        #print(filling_level,next_date.isoformat())
        update_fillingLevel(filling_level,next_date.isoformat())
        time.sleep(5)

fill_fake_data()