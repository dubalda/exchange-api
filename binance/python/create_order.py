import os

from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *

g_api_key = os.environ.get('binance_api')
g_secret_key = os.environ.get('binance_secret')


request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)

result = request_client.get_mark_price(symbol="BTCUSDT")

print("======= Mark Price =======")
PrintBasic.print_obj(result)
print("==========================")