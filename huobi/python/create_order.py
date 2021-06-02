import time
import huobi

#huobi.swap_openorders('btc-usd')

contract_code = 'btc-usd'

current_price = float(huobi.swap_mark_price_kline(contract_code = contract_code, period = '1min', size = '1'))
print(contract_code, "price $", str(current_price))

#huobi.swap_order(contract_code = contract_code, price = '10000')

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


grid_low_price = int(0.67 * start_price)
grid_high_price = int(0.87 * start_price)
grid_step = (grid_high_price - grid_low_price) // cont_quarter
print(">>> Grid 13%-33%:", cont_quarter, "CONT from ", grid_low_price, " to ", grid_high_price, " with step ", grid_step)
for cont in range(0, cont_quarter):
  time.sleep(0.05)
  next_price = str(grid_low_price + (cont * grid_step))
  print(">>> Grid 13%-33%, CONT", cont, ": Price", next_price)
  huobi.swap_order(contract_code = contract_code, price = next_price)


grid_low_price = int(0.88 * start_price)
grid_high_price = int(0.95 * start_price)
grid_step = (grid_high_price - grid_low_price) // cont_quarter
print(">>> Grid 5%-12%:", cont_quarter, "CONT from ", grid_low_price, " to ", grid_high_price, " with step ", grid_step)
for cont in range(0, cont_quarter):
  time.sleep(0.01)
  next_price = grid_low_price + (cont * grid_step)
  print(">>> Grid 5%-12%, CONT", cont, ": Price", next_price)
  huobi.swap_order(contract_code = contract_code, price = next_price)


grid_low_price = int(0.96 * start_price)
grid_high_price = int(0.99 * start_price)
grid_step = (grid_high_price - grid_low_price) // cont_quarter
print(">>> Grid 1%-4%:", cont_quarter, "CONT from ", grid_low_price, " to ", grid_high_price, " with step ", grid_step)
for cont in range(0, cont_quarter):
  time.sleep(0.01)
  next_price = grid_low_price + (cont * grid_step)
  print(">>> Grid 1%-4%, CONT", cont, ": Price", next_price)
  huobi.swap_order(contract_code = contract_code, price = next_price)





print("DONE")
print("==========================")
