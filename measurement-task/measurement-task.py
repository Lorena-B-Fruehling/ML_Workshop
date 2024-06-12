import requests
import time

url = "http://worldtimeapi.org/api/timezone/Europe/Berlin"
response = requests.get(url)
print(response.elapsed.total_seconds())

for i in range(10):
    response = requests.get(url)
    print(response.elapsed.total_seconds())
    time.sleep(0.1)

# close connection to db