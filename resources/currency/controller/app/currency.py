import os
import json

#from flask import Flask, jsonify, redirect, render_template, request

from pathlib import Path  # python3 only

from google.cloud import secretmanager

from alpha_vantage.foreignexchange import ForeignExchange

app = Flask(__name__)

secrets = secretmanager.SecretManagerServiceClient()

ALPHAVANTAGE_KEY = secrets.access_secret_version("projects/"+PROJECT_ID+"/secrets/alpha-vantage-secret/versions/1").payload.data.decode("utf-8")

sink_url = os.getenv('K_SINK')


def make_msg(message):
    msg = '{"msg": "%s"}' % (message)
    return msg


def get_currency():
    curr1='JPY'
    curr2='USD'
    fx = ForeignExchange(key=ALPHAVANTAGE_KEY)
    data, _ = fx.get_currency_exchange_rate(
            from_currency=curr1, to_currency=curr2)
    exrate = float(data['5. Exchange Rate'])        
    return exrate


while True:
    headers = {'Content-Type': 'application/cloudevents+json'}
    body = get_currency()
    requests.post(sink_url, data=json.dumps(body), headers=headers)
    time.sleep(15)