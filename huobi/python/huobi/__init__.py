import requests
import json
import hmac
import hashlib
import base64
from urllib.parse import urlencode
from datetime import datetime
import os

global AccessKeyId
global SecretKey
global timestamp
global params
global base_uri

def init():
  #Get all Accounts of the Current User
  AccessKeyId = os.environ.get('accessKey')
  SecretKey = os.environ.get('secretKey')
  timestamp = str(datetime.utcnow().isoformat())[0:19]
  params = urlencode({'AccessKeyId': AccessKeyId,
                    'SignatureMethod': 'HmacSHA256',
                    'SignatureVersion': '2',
                    'Timestamp': timestamp
                   })
  base_uri = 'api.hbdm.vn'


def swap_openorders(contract_code: 'str'):
    init()
    body = {"contract_code":contract_code   }
    method = 'POST'
    endpoint = '/swap-api/v1/swap_openorders'
    pre_signed_text = method + '\n' + base_uri + '\n' + endpoint + '\n' + params
    hash_code = hmac.new(SecretKey.encode(), pre_signed_text.encode(), hashlib.sha256).digest()
    signature = urlencode({'Signature': base64.b64encode(hash_code).decode()})
    url = 'https://' + base_uri + endpoint + '?' + params + '&' + signature
    response = requests.request(method, url, json = body)
    swap_openorders = json.loads(response.text)
    print(swap_openorders)
