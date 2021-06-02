import huobi

#huobi.swap_openorders('btc-usd')

huobi.swap_mark_price_kline(contract_code = 'btc-usd', period = '1min', size = '1')