import huobi

#huobi.swap_openorders('btc-usd')

contract_code = 'btc-usd'

price = huobi.swap_mark_price_kline(contract_code = contract_code, period = '1min', size = '1')
print(contract_code, "price $", price)

huobi.swap_order(contract_code = contract_code, price = '10000')