from pykrx import stock

'''
tickers = stock.get_market_ticker_list("20201223",market="KOSDAQ")
print(tickers)
# KOSPI(default), KOSDAK, KONEX, ALL

name = stock.get_market_ticker_name("000660")
print(name)


df = stock.get_market_ohlcv_by_date("20200810", "20201212", "005930")
print(df.head(2))
#시작일, 종료일, 종목번호

import time
for ticker in stock.get_market_ticker_list():
    df = stock.get_market_ohlcv_by_date("20201210", "20201210", ticker)
    #print(df.head())
    #time.sleep(0.01)
    print(ticker)
'''
df = stock.get_market_ohlcv_by_ticker("20201217")
print(df['시가총액'])
print(df.head(3))


#df = stock.get_market_price_change_by_ticker("20201217", "20201218")
#print(df)


import plotly.express as px
import numpy as np
#df = px.data.gapminder().query("year == 2007")
#df["world"] = "world" # in order to have a single root node
fig = px.treemap(df, path=['종목명'], values='시가총액',
                  color='시가총액', #hover_data=['iso_alpha'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df['시가총액'], weights=df['시가총액']))
fig.show()
