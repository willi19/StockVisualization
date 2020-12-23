from website import krx
import datetime
import pandas as pd

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

df = krx.get_market_cap_by_ticker(get_nearest_business_day_in_a_week())

print(df)