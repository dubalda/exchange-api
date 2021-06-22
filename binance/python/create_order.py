import os

from binance_d import RequestClient
from binance_d.constant.test import *
from binance_d.base.printobject import *
from binance_d.model.constant import *
import time

g_api_key = os.environ.get('binance_api')
g_secret_key = os.environ.get('binance_secret')
g_url = os.environ.get('binance_futures_url')

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key, url=g_url)

# Change leverage to x2
result = request_client.change_initial_leverage(symbol="BTCUSD_PERP", leverage=2)
print("== Change leverage to x2 =")
PrintBasic.print_obj(result)
print("==========================")

result = request_client.get_mark_price(symbol="BTCUSD_PERP")
print("======= Mark Price =======")
PrintMix.print_data(result)
print("==========================")
current_price = result[0].markPrice
print("Current price:", current_price)

input_high_price = input("Input max order PRICE (current price "+str(current_price)+"$): ")
try:
  high_price = int(input_high_price)
except ValueError:
  print(input_high_price, "not number")
  exit()
if high_price > current_price:
  print(high_price, "must be less then", current_price)
  exit()

input_low_price = input("Input min order PRICE: ")
try:
  low_price = int(input_low_price)
except ValueError:
  print(input_low_price, "not number")
  exit()
if low_price > high_price:
  print(low_price, "must be less then", high_price)
  exit()

input_cont_total = input("Input CONT total: ")
try:
  cont_total = int(input_cont_total)
except ValueError:
  print(input_cont_total, "not number")
  exit()
if cont_total < 1:
  print(cont_total, "must be more then 0")
  exit()
low_cont_total = cont_total // 3 * 2
high_cont_total = cont_total // 3

mid_price = int(low_price + (high_price - low_price) // 2)
low_grid_step = (mid_price - low_price) // low_cont_total
high_grid_step = (mid_price - low_price) // high_cont_total
print(">>> Low grid:", low_cont_total, "CONT from ", low_price, " to ", mid_price, " with step ", low_grid_step)
print(">>> High grid:", high_cont_total, "CONT from ", mid_price, " to ", high_price, " with step ", high_grid_step)

input("Press Enter to continue...")

for cont in range(1, low_cont_total + 1):
  time.sleep(0.02)
  next_price = low_price + (cont * low_grid_step)
  print(">>> CONT", cont, ": Price", next_price)
  result = request_client.post_order(symbol="BTCUSD_PERP", side=OrderSide.BUY, ordertype=OrderType.LIMIT, price=next_price, quantity=1, timeInForce=TimeInForce.GTC)

for cont in range(1, high_cont_total + 1):
  time.sleep(0.02)
  next_price = mid_price + (cont * high_grid_step)
  print(">>> CONT", cont, ": Price", next_price)
  result = request_client.post_order(symbol="BTCUSD_PERP", side=OrderSide.BUY, ordertype=OrderType.LIMIT, price=next_price, quantity=1, timeInForce=TimeInForce.GTC)

# Get all orders
#result = request_client.get_all_orders(symbol="BTCUSD_PERP")
#print("==========================")
#PrintMix.print_data(result)
#print("==========================")

print("DONE")
print("==========================")