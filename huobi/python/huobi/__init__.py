import requests
import json
import hmac
import hashlib
import base64
from urllib.parse import urlencode

def swap_openorders(contract_code: 'str'):
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
