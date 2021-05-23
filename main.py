# Import Flask so that we can create an app instance
import sqlite3
from flask import Flask, request, url_for, render_template, flash
from flask import g
import jwt   # PyJWT
import uuid
import requests
import websocket
import json
from flask_socketio import SocketIO, send, emit
from eventlet import wsgi
import eventlet
from upbitpy import Upbitpy
import logging

DATABASE = 'deomps5.db'
# UpbitPy init
krw_markets = []
def print_tickers(items):
    for it in items:
        logging.info('{}: {} won'.format(it['market'], it['trade_price']))

app = Flask(__name__)
app.config.from_object(__name__)
SocketIO = SocketIO(app)

#UPBIT ACCESS
#Access Key : dqZ29pX3nfA8KyxmiYyRt9UwzBOW4a8TwRs34Er7
#Secret Key : V6Hd527RnXmqsEbq1qP6sMBpxw0po7zjbBwHr9L4

payload = {
    'access_key': 'dqZ29pX3nfA8KyxmiYyRt9UwzBOW4a8TwRs34Er7',
    'nonce': str(uuid.uuid4()),
}
jwt_token = jwt.encode(payload, 'V6Hd527RnXmqsEbq1qP6sMBpxw0po7zjbBwHr9L4')
authorization_token = 'Bearer {}'.format(jwt_token)

## For Upbit Realtime Price check
# try:
#     import thread
# except ImportError:
#     import _thread as thread
# import time


def on_message(ws, message):
    get_message = json.loads(message)
    print(get_message["code"],'\'s Real Time Price: ', get_message["trade_price"])
    handle_json(get_message);

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("close")

# def on_open(ws):
#     def run():
#         sendData = '[{"ticket":"test"},{"type":"ticker","codes":['
#         for market in krw_markets:
#             sendData += '"' + market + '"'
#             if krw_markets.index(market) != len(krw_markets)-1:
#                 sendData += ','
#         sendData += '],"isOnlySnapshot":true}]'
#         ws.send(sendData)
#     time.sleep(10)
#     thread.start_new_thread(on_open, (ws))

# All Flask app must create an app instance like this with the name of
# the main module:


# DB connection
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# query function
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    print(rv)
  #  tnames = []
  #  if len(rv) is not 0:
      #  for t in cur.description:
      #      tnames.append(t[0])
      #  rv.insert(0, tnames)
    cur.close()
    return (rv[0] if rv else None) if one else rv

# def realtime_connect():
#     """  ws = websocket.WebSocketApp("wss://api.upbit.com/websocket/v1",
#                                 on_message=on_message,
#                                 on_error=on_error,
#                                 on_close=on_close)
#     ws.on_open = on_open
#     thread.start_new_thread(ws.run_forever, ())
#     """
#     url = "https://api.upbit.com/v1/ticker"
#     markets = ""
#     for market in krw_markets:
#         markets += market
#         if krw_markets.index(market) != len(krw_markets) - 1:
#             markets += ','
#     querystring = {"markets": markets}
#     headers = {"Accept": "application/json"}
#     response = requests.request("GET", url, headers=headers, params=querystring)
#     for market in response.json():
#         print(market["market"],'\'s Real Time Price: ', market["trade_price"])
#     time.sleep(10)
#     thread.start_new_thread(realtime_connect, ())

# Invoke this one with http://127.0.0.1:5000
@app.route('/')
def index():
    # upbit = Upbitpy()
    # markets = upbit.get_market_all()
    # for market in markets:
    #     if 'KRW-' in market['market']:
    #         krw_markets.append(market['market'])
    # realtime_connect()
#    headers = {"Authorization": authorization_token}
#    res = requests.get('https://api.upbit.com/v1/ticker?markets=KRW-ETH', headers=headers).json()
#    print(res)
    return render_template('base.html')

@app.route('/main')
def main():
    return render_template('landing-2.html')

# Flask SocketIO handler
@SocketIO.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

@SocketIO.on('json')
def handle_json(json):
    emit(json, json=True)

@SocketIO.on('message')
def handle_message(message):
    emit('json',message)

# Now, run the app as a server in debug mode or public mode
if __name__ == '__main__':
    wsgi.server(eventlet.listen(('127.0.0.1', 5000)), app)
    SocketIO.run(app)
    # app.run(debug=True)        # Debug mode will reload files when changed.
    # app.run(host='0.0.0.0')  # To make the server listen on all public IPs.
