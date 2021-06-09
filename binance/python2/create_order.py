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
current_price = result[0].markPrice
print("Current price:", current_price)

from binance_d.model.constant import *


input_cont_total = input("Input CONT total: ")

try:
  cont_total = int(input_cont_total)
except ValueError:
  print(input_cont_total, "not number")
  exit()

if cont_total < 1:
  print(cont_total, "must be more then 0")
  exit()

input_start_price = input("Input start PRICE (current price "+str(current_price)+"$): ")

try:
  start_price = int(input_start_price)
except ValueError:
  print(input_start_price, "not number")
  exit()

if start_price > current_price:
  print(start_price, "must be less then", current_price)
  exit()


# Change leverage to x2

result = request_client.change_initial_leverage(symbol="BTCUSD_PERP", leverage=2)
print("== Change leverage to x2 =")
PrintBasic.print_obj(result)
print("==========================")

import time

grid_low_price = int(0.5 * start_price)
grid_high_price = int(start_price)
grid_step = (grid_high_price - grid_low_price) // cont_total
print(">>> Grid 50%-100%:", cont_total, "CONT from ", grid_low_price, " to ", grid_high_price, " with step ", grid_step)
for cont in range(1, cont_total + 1):
  time.sleep(0.02)
  next_price = grid_low_price + (cont * grid_step)
  print(">>> CONT", cont, ": Price", next_price)
  result = request_client.post_order(symbol="BTCUSD_PERP", side=OrderSide.BUY, ordertype=OrderType.LIMIT, price=next_price, quantity=1, timeInForce=TimeInForce.GTC)


# Get all orders

#result = request_client.get_all_orders(symbol="BTCUSD_PERP")
#print("==========================")
#PrintMix.print_data(result)
#print("==========================")



print("DONE")
print("==========================")