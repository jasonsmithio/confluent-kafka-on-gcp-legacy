import os
import json
from google.cloud import bigquery

client = bigquery.Client()

quotes = []

# Perform a query.
QUERY = 'SELECT bid_price FROM (SELECT rand() as random,bid_price FROM `bigquery-samples.nasdaq_stock_quotes.quotes` ORDER BY random) LIMIT 20'

query_job = client.query(QUERY)  # API request
rows = query_job.result()
for row in rows:
    price = row.bid_price
    quotes.append(price)
print(quotes)