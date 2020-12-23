import pandas as pd 
import requests 

html = requests.get('https://finance.naver.com/item/frgn.nhn?code=005930&page=1') 

table = pd.read_html(html.text)

print(table)