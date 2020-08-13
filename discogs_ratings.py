import sys
import json

from urllib import request
from urllib.parse import parse_qsl, urlparse

import oauth2


CONSUMER_KEY = ''
CONSUMER_SECRET = ''

REQUEST_TOKEN_URL = 'https://api.discogs.com/oauth/request_token'
AUTHORIZE_URL = 'https://www.discogs.com/oauth/authorize'
ACCESS_TOKEN_URL = 'https://api.discogs.com/oauth/access_token'

USER_AGENT = 'discogs_api_example/1.0'

consumer = oauth2.Consumer(CONSUMER_KEY, CONSUMER_SECRET)
client = oauth.Client(consumer)

resp, content = client.request(REQUEST_TOKEN_URL, 'POST',
                               headers={'User-Agent': USER_AGENT})

if resp['status'] != 200:
    sys.exit(f"Invalid response {resp['status_code']}")

request_token = dict(parse_psql(content.decode('utf-8')))
