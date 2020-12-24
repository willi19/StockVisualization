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
df_merge['종목등락']=df_merge['종목명']+"\n"+df_merge['등락률'].astype(str)+"%"
print(df_merge['종목등락'])
df_merge['연습'] =""
df_merge['연습'][0:300] = "1"
df_merge['연습'][300:600] = "2"
df_merge['연습'][600:900] = "3"
df_merge['연습'][900:1200] = "4"
df_merge['연습'][1200:1500] = "5"
df_merge['연습'][1500:1800] = "6"
df_merge['연습'][1800:2100] = "7"
df_merge['연습'][2100:] = "8"


print(len(df_merge))
fig = px.treemap(df_merge, path=['연습','종목등락'], values='시가총액',
                  color='등락률', 
                  color_continuous_scale=[(0, "rgb(246,53,56)"), (0.1666, "rgb(191,64,69)"), (0.33333, "rgb(139,68,78)"), (0.5, "rgb(65,69,84)"), (0.6666, "rgb(53,118,78)"), (0.8333, "rgb(47,158,79)"), (1, "rgb(48,204,90)")],
                  range_color = [-3,3],
                  color_continuous_midpoint=np.average(df_merge['등락률'], weights=df_merge['시가총액']))
fig.update_traces(textposition="middle center",
                  textfont_color = "rgb(256,256,256)",
                  textinfo="label", 
                  marker_line_width= 0,
                  hoverlabel_bgcolor="rgb(256,256,0)",
                  selector=dict(type='treemap'))
fig.show()