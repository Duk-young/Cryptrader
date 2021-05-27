# Import Flask so that we can create an app instance
import sqlite3
import threading

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

DATABASE = 'cryptoCurrencies.db'
# UpbitPy init
krw_markets = []


# def print_tickers(items):
#     for it in items:
#         logging.info('{}: {} won'.format(it['market'], it['trade_price']))

app = Flask(__name__)
app.config.from_object(__name__)
socketio = SocketIO(app)
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
try:
    import thread
except ImportError:
    import _thread as thread
import time

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

def realtime_connect():
    """  ws = websocket.WebSocketApp("wss://api.upbit.com/websocket/v1",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    thread.start_new_thread(ws.run_forever, ())
    """
    url = "https://api.upbit.com/v1/ticker"
    markets = ""
    for market in krw_markets:
        markets += market
        if krw_markets.index(market) != len(krw_markets) - 1:
            markets += ','
    querystring = {"markets": markets}
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    #url = "https://api.upbit.com/v1/market/all"
    toClient = {}
    for market in response.json():
        #print(market["market"],'\'s Real Time Price: ', market["trade_price"])
        toClient[market["market"]] = [market["trade_price"],market["high_price"],market["low_price"],market["acc_trade_price"],market["prev_closing_price"],market["change_price"],market["change_rate"], market["change"]]
    return toClient
   # handle_json(toClient,sid);
   # print("json request delivered.")
   # time.sleep(5)
   # thread.start_new_thread(realtime_connect, (sid,))

# Invoke this one with http://127.0.0.1:5000

@app.route('/test/')
def test():
    return render_template('test.html')


@app.route('/')
def index():
    return render_template('base.html')

# Flask SocketIO handler
@app.route('/main/')
def mainPage():
    return render_template('login.html')
@app.route('/landing/')
def landing():
    return render_template('landing.html')
@app.route('/prices')
def prices():
    coinList = query_db('SELECT * FROM Coins')
    print(coinList)
    return render_template('prices.html', list=coinList)

@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')


@socketio.on('my event')
def handle_my_custom_event(sid):
    print('received json: ' + str(sid))
    #socketio.emit('json', realtime_connect())
    socketio.emit('json', realtime_connect(), to=sid)

@socketio.on('create table')
def emitJson(sid):
    socketio.emit('create table', realtime_connect(), to=sid)

@socketio.on('update')
def update(json):
    socketio.emit('update', json, broadcast=True)


class ThreadCount(object):
    def __init__(self):
        self = []
    def append(self, thread):
        self = [thread]
    def getCount(self):
        return len(self)
    def join(self):
        self[0].join()
"""
@socketio.on('realtime')
def realtime_data(json, methods=['GET', 'POST']):
    socketio.send('realtime', json)
"""
# Now, run the app as a server in debug mode or public mode
if __name__ == '__main__':
    upbit = Upbitpy()
    markets = upbit.get_market_all()
    for market in markets:
        if 'KRW-' in market['market']:
            krw_markets.append(market['market'])
    #wsgi.server(eventlet.listen(('127.0.0.1', 5000)), app
    socketio.run(app, debug=True)
  #  app.run(debug=True)        # Debug mode will reload files when changed.
    # app.run(host='0.0.0.0')  # To make the server listen on all public IPs.