from website import krx
import datetime
import pandas as pd
import plotly.express as px
import numpy as np

def _datetime2string(dt, freq='d'):
    if freq.upper() == 'Y':
        return dt.strftime("%Y")
    elif freq.upper() == 'M':
        return dt.strftime("%Y%m")
    else:
        return dt.strftime("%Y%m%d")

def get_nearest_business_day_in_a_week():
    curr = datetime.datetime.now()
    prev = curr - datetime.timedelta(days=7)
    curr = _datetime2string(curr)
    prev = _datetime2string(prev)
    df = krx.get_index_ohlcv_by_date(prev, curr, "1001")
    return df.index[-1].strftime("%Y%m%d")

date = get_nearest_business_day_in_a_week()

df_cap = krx.get_market_ohlcv_by_ticker(date,"ALL")[['종목명', '시가총액']]
df_change = krx.get_market_price_change_by_ticker(date, date)[['종목명', '등락률']]

"""
print(df_cap.head(3))
print(df_change.head(3))
print(get_nearest_business_day_in_a_week())
"""

df_merge = pd.merge(df_cap,df_change,how = 'inner',on='종목명')
print(df_merge.head(3))

fig = px.treemap(df_merge, path=['종목명'], values='시가총액',
                  color='등락률', #hover_data=['iso_alpha'],
                  color_continuous_scale='RdBu',
                  color_continuous_midpoint=np.average(df_merge['등락률'], weights=df_merge['시가총액']))

fig.show()