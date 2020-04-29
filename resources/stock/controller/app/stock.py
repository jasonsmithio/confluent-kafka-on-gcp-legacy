import os
import json
import requests
import time

from pathlib import Path  # python3 only

from google.cloud import secretmanager

from google.cloud import bigquery

secrets = secretmanager.SecretManagerServiceClient()

sink_url = os.getenv('K_SINK')

client = bigquery.Client()

quotes = []

# Perform a query.
QUERY = 'SELECT bid_price FROM (SELECT rand() as random,bid_price FROM `bigquery-samples.nasdaq_stock_quotes.quotes` ORDER BY random) LIMIT 20'

def make_msg(message):
    msg = '{"msg": "%s"}' % (message)
    return msg


def get_query():
    query_job = client.query(QUERY)  # API request
    rows = query_job.result()
    for row in rows:
        price = row.bid_price
        quotes.append(price)
    return quotes
    

while True:
    headers = {'Content-Type': 'application/cloudevents+json'}
    body = get_query()
    requests.post(sink_url, data=json.dumps(body), headers=headers)
    time.sleep(30)