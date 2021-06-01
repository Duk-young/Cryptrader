# Import Flask so that we can create an app instance
import sqlite3
import threading

from flask import Flask, request, url_for, render_template, session, redirect, flash
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
app.secret_key = 'cse305finalproejct'
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
    print("From query: " + str(rv))
  #  tnames = []
  #  if len(rv) is not 0:
      #  for t in cur.description:
      #      tnames.append(t[0])
      #  rv.insert(0, tnames)
    cur.close()
    return (rv[0] if rv else None) if one else rv

def realtime_holdings(holdings):
    if len(holdings) == 0:
        return None
    url = "https://api.upbit.com/v1/ticker"
    markets = ""
    for coin in holdings:
        markets += coin[0]
        if holdings.index(coin) != len(holdings) - 1:
            markets += ','
    print(markets)
    querystring = {"markets": markets}
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    #url = "https://api.upbit.com/v1/market/all"
    print(response)
    toClient = {}
    for market in response.json():
        print(market["market"],'\'s Real Time Price: ', market["trade_price"])
        toClient[market["market"]] = [market["trade_price"]]
    return toClient
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


def realtime_one():
    url = "https://api.upbit.com/v1/candles/minutes/5?market=KRW-BTC&count=20"
    headers = {"Accept": "application/json"}
    response = requests.request("GET", url, headers=headers)
    toClient = {}
    for market in response.json():
        toClient[market["candle_date_time_kst"]] = [market["candle_date_time_kst"],market["low_price"],market["trade_price"],market["opening_price"],market["high_price"]]
    return toClient

# Invoke this one with http://127.0.0.1:5000
@app.before_request
def check_session():
    if 'user_info' in session:
        user = session['user_info']
        g.user = user
    else:
        g.user = None


# Flask SocketIO handler
@app.route('/',methods=['GET','POST'])
def mainPage():
    if request.method == 'POST':
        session.pop('user_info', None)
        if "new_uname" in request.form:
            uname = request.form['new_uname']
            password = request.form['password']
            password_repeat = request.form['password_repeat']
            if password==password_repeat :
                user_check = query_db('SELECT uid FROM User_login WHERE uname = ?', [uname])
                if len(user_check) == 0:
                    uid = query_db('SELECT COUNT(*) FROM User_login')[0][0] + 1
                    print("uid: "+ str(uid))
                    conn = get_db()
                    cur = conn.cursor()
                    cur.execute('INSERT INTO User_login (uid, uname, password) VALUES (?, ?, ?)', [uid, uname, password])
                    cur.execute('INSERT INTO User_info (uid, budget) VALUES (?, ?)', [uid, 10000000])
                    conn.commit()
                    cur.close()
                    flash("Successfully registered! Please sign in", 'register_success')
                else:
                    flash("Username already exists. Please try with other user name", 'register_fail')
            else:
                flash("Passwords do not match", 'register_fail')
        else:
            uname = request.form['uname']
            password = request.form['password']
            user = query_db('SELECT uid, uname FROM User_login WHERE uname = ? AND password = ?', [uname, password])
            if len(user) != 0:
                session['user_info'] = user[0]
                return redirect(url_for('prices'))
            flash("Invalid username or password", 'sign_in')
    return render_template('landing.html')
@app.route('/landing/')
def landing():
    return render_template('landing.html')
    
@app.route('/prices', methods=['POST','GET'])
def prices():
    coinList = query_db('SELECT * FROM Coins')
    print(coinList)
    return render_template('prices.html', list=coinList)

@app.route('/prices/<code>')
def coinSpec(code):
    return render_template('chart.html', code=code)

@app.route('/profile')
def profile():
    if g.user is None:
        flash("Sign in required", 'sign_in')
        return redirect('/')
    budget = query_db('SELECT budget FROM User_info WHERE uid = ?', [g.user[0]])[0][0]
    holdings = query_db('SELECT code, num, avg_price FROM User_holding WHERE uid = ?', [g.user[0]])
    names = []
    count = 0
    for coin in holdings:
        name = query_db('SELECT name FROM Coins WHERE code = ?', [coin[0]])[0]
        coin = coin[:1]+ name +coin[1:]
        holdings[count] = coin
        count += 1
    print(holdings)
    return render_template('profile.html', budget=budget, holdings=holdings)
@app.route('/signout')
def signout():
    session.pop('user_info', None)
    g.user = None
    return redirect('/')

@socketio.on('my event')
def handle_my_custom_event(sid):
    print('received json: ' + str(sid))
    #socketio.emit('json', realtime_connect())
    socketio.emit('json', realtime_connect(), to=sid)

@socketio.on('my holdings')
def handle_my_holdings(holdings):
    #print('[%s]' % ', '.join(map(str, holdings)))
    socketio.emit('json', realtime_holdings(holdings))

@socketio.on('one coin')
def handle_one_coin(sid):
    print('received json: ' + str(sid))
    #socketio.emit('json', realtime_connect())
    socketio.emit('json', realtime_one())


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


class User:
    def __init__(self, uid, uname, password):
        self.id = uid
        self.uname = uname
        self.password = password

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