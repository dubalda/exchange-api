import os

from binance_d import RequestClient
from binance_d.constant.test import *
from binance_d.base.printobject import *

g_api_key = os.environ.get('binance_api')
g_secret_key = os.environ.get('binance_secret')
g_url = os.environ.get('binance_futures_url')

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key, url=g_url)

result = request_client.get_mark_price(symbol="BTCUSD_PERP")

print("======= Mark Price =======")
PrintMix.print_data(result)
print("==========================")

