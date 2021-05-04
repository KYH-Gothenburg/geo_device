import time

import requests
import json
from time import sleep

def main():
    data = requests.get('http://127.0.0.1:5000/api/v1.0/coords?country=se&num_steps=50')
    path = json.loads(data.text)['path']

    converted_path = []
    for pos in path:
        lng, lat = pos.split(', ')
        converted_path.append({
            'long': lng,
            'lat': lat
        })


    # http://127.0.0.1:5001/api/v1.0/positions
    # Simulated walk
    for step in converted_path:
        data = {
            'client_id': 65,
            'timestamp': time.time(),
            'position': step
        }
        requests.post('http://127.0.0.1:5001/api/v1.0/positions',json=data)
        sleep(2)



if __name__ == '__main__':
    main()