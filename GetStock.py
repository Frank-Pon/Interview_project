import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_stock(stock_code):
    url = f'https://tw.stock.yahoo.com/quote/{stock_code}.TW'
    headers = {
    'User-Agent':'Mozilla/5.0'
    #
    }
    res = requests.get(url,headers=headers)
    soup = BeautifulSoup(res.text,'html.parser')
    #

    stock_name = soup.find('h1',class_='C($c-link-text) Fw(b) Fz(24px) Mend(8px)')
    stock_price = soup.find('span',class_='Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)')
    now = datetime.now().strftime('%Y / %m / %d - %H : %M : %S')
    #
    #<h1 class="C($c-link-text) Fw(b) Fz(24px) Mend(8px)">台積電</h1>
    #<span class="C($c-icon) Fz(24px) Mend(20px)">2330</span>
    #<span class="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)">972</span>

    if stock_name and stock_price:
        return {
            'stock_name':stock_name.text,
            'stock_num':stock_code,
            'stock_price':stock_price.text,
            'time':now,
            'currency':'新台幣',
            'status':'Success'
        }
    #
    else:
        return {
            'stock_num':stock_code,
            'status':'Not found'
        }