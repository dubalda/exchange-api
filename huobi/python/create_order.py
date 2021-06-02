import os
from datetime import datetime
from urllib.parse import urlencode

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

import huobi

huobi.swap_openorders('btc-usd')