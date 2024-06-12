import psycopg2
import requests
import time
from datetime import datetime

urls = [
        "http://worldtimeapi.org/api/timezone/Europe/Berlin",
        "http://google.de/",
        "http://heise.de/"
        ]

insert_query = """
        INSERT INTO public.responsetimes (url, measuretime, responsetime) VALUES (%s, %s, %s)
        """

CONNECTION = "postgres://postgres:password@db:5432/sampledata"
conn = psycopg2.connect(CONNECTION)
cursor = conn.cursor()

while True:
        for url in urls:
                response = requests.get(url)
                print(url, response.elapsed.total_seconds())
                cursor.execute(insert_query, (url, datetime.now(), response.elapsed.total_seconds()*100000))
                conn.commit()
        time.sleep(0.2)
