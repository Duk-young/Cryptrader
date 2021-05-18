# Import Flask so that we can create an app instance
import sqlite3
from flask import Flask, request, url_for, render_template, flash
from flask import g
import jwt   # PyJWT
import uuid
import requests
from flask_wtf import Form

#UPBIT ACCESS
#Access Key : dqZ29pX3nfA8KyxmiYyRt9UwzBOW4a8TwRs34Er7
#Secret Key : V6Hd527RnXmqsEbq1qP6sMBpxw0po7zjbBwHr9L4
payload = {
    'access_key': 'dqZ29pX3nfA8KyxmiYyRt9UwzBOW4a8TwRs34Er7',
    'nonce': str(uuid.uuid4()),
}
jwt_token = jwt.encode(payload, 'V6Hd527RnXmqsEbq1qP6sMBpxw0po7zjbBwHr9L4')
authorization_token = 'Bearer {}'.format(jwt_token)
# All Flask app must create an app instance like this with the name of
# the main module:

DATABASE = 'deomps5.db'


app = Flask(__name__)
app.config.from_object(__name__)
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

# Invoke this one with http://127.0.0.1:5000
@app.route('/')
def index():
    headers = {"Authorization": authorization_token}
    res = requests.get('https://api.upbit.com/v1/ticker?markets=KRW-ETH', headers=headers).json()
    print(res)
    return render_template('base.html')



# Now, run the app as a server in debug mode or public mode
if __name__ == '__main__':
    app.run(debug=True)        # Debug mode will reload files when changed.
    # app.run(host='0.0.0.0')  # To make the server listen on all public IPs.
