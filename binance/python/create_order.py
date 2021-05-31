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

if cont_total < 4:
  print(cont_total, "must be more then 4")
  exit()

cont_quarter = cont_total // 4

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

grid_low_price = int(0.67 * start_price)
grid_high_price = int(0.87 * start_price)
grid_step = (grid_high_price - grid_low_price) // cont_quarter
print(">>> Grid 13%-33%:", cont_quarter, "CONT from ", grid_low_price, " to ", grid_high_price, " with step ", grid_step)
for cont in range(0, cont_quarter):
  time.sleep(0.01)
  next_price = grid_low_price + (cont * grid_step)
  print(">>> Grid 13%-33%, CONT", cont, ": Price", next_price)
  result = request_client.post_order(symbol="BTCUSD_PERP", side=OrderSide.BUY, ordertype=OrderType.LIMIT, price=next_price, quantity=1, timeInForce=TimeInForce.GTC)


grid_low_price = int(0.88 * start_price)
grid_high_price = int(0.95 * start_price)
grid_step = (grid_high_price - grid_low_price) // cont_quarter
print(">>> Grid 5%-12%:", cont_quarter, "CONT from ", grid_low_price, " to ", grid_high_price, " with step ", grid_step)
for cont in range(0, cont_quarter):
  time.sleep(0.01)
  next_price = grid_low_price + (cont * grid_step)
  print(">>> Grid 5%-12%, CONT", cont, ": Price", next_price)
  result = request_client.post_order(symbol="BTCUSD_PERP", side=OrderSide.BUY, ordertype=OrderType.LIMIT, price=next_price, quantity=1, timeInForce=TimeInForce.GTC)


grid_low_price = int(0.96 * start_price)
grid_high_price = int(0.9999 * start_price)
grid_step = (grid_high_price - grid_low_price) // cont_quarter
print(">>> Grid 1%-4%:", cont_quarter, "CONT from ", grid_low_price, " to ", grid_high_price, " with step ", grid_step)
for cont in range(0, cont_quarter):
  time.sleep(0.01)
  next_price = grid_low_price + (cont * grid_step)
  print(">>> Grid 1%-4%, CONT", cont, ": Price", next_price)
  result = request_client.post_order(symbol="BTCUSD_PERP", side=OrderSide.BUY, ordertype=OrderType.LIMIT, price=next_price, quantity=1, timeInForce=TimeInForce.GTC)



# Get all orders

#result = request_client.get_all_orders(symbol="BTCUSD_PERP")
#print("==========================")
#PrintMix.print_data(result)
#print("==========================")



print("DONE")
print("==========================")