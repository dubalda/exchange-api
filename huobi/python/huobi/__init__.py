import requests
import json
import hmac
import hashlib
import base64
from urllib.parse import urlencode
from datetime import datetime
import os

global base_uri
global AccessKeyId
global SecretKey

base_uri = 'api.hbdm.vn'
AccessKeyId = os.environ.get('accessKey')
SecretKey = os.environ.get('secretKey')

def signature(pre_signed_text: 'str'):
  hash_code = hmac.new(SecretKey.encode(), pre_signed_text.encode(), hashlib.sha256).digest()
  signature = urlencode({'Signature': base64.b64encode(hash_code).decode()})
  return signature

def swap_openorders(contract_code: 'str'):
    body = {"contract_code":contract_code}
    method = 'POST'
    endpoint = '/swap-api/v1/swap_openorders'
    timestamp = str(datetime.utcnow().isoformat())[0:19]
    params = urlencode({'AccessKeyId': AccessKeyId,
                    'SignatureMethod': 'HmacSHA256',
                    'SignatureVersion': '2',
                    'Timestamp': timestamp
                   })
    pre_signed_text = method + '\n' + base_uri + '\n' + endpoint + '\n' + params
    url = 'https://' + base_uri + endpoint + '?' + params + '&' + signature(pre_signed_text)
    response = requests.request(method, url, json = body)
    swap_openorders = json.loads(response.text)
    print(swap_openorders)


def swap_mark_price_kline(contract_code: 'str', period: 'str', size: 'str'):
    body = {"contract_code":contract_code}
    method = 'GET'
    endpoint = '/index/market/history/swap_mark_price_kline'
    params = urlencode({'contract_code': contract_code,
                    'period': period,
                    'size': size
                   })
    pre_signed_text = method + '\n' + base_uri + '\n' + endpoint + '\n' + params
    url = 'https://' + base_uri + endpoint + '?' + params + '&' + signature(pre_signed_text)
    response = requests.request(method, url)
    swap_openorders = json.loads(response.text)
    print(swap_openorders)


