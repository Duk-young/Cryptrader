
# Python 3

import jwt   # PyJWT 
import uuid
import requests


#UPBIT ACCESS
#Access Key : dqZ29pX3nfA8KyxmiYyRt9UwzBOW4a8TwRs34Er7
#Secret Key : V6Hd527RnXmqsEbq1qP6sMBpxw0po7zjbBwHr9L4

payload = {
    'access_key': 'dqZ29pX3nfA8KyxmiYyRt9UwzBOW4a8TwRs34Er7',
    'nonce': str(uuid.uuid4()),
}
jwt_token = jwt.encode(payload, 'V6Hd527RnXmqsEbq1qP6sMBpxw0po7zjbBwHr9L4')
authorization_token = 'Bearer {}'.format(jwt_token)


url = "https://api.upbit.com/v1/ticker?markets=KRW-BTC"

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers)

print(response.json()[0]['trade_date'])
