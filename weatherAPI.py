import requests #發送網頁請求庫
from bs4 import BeautifulSoup #爬蟲庫
from datetime import datetime #時間庫

url = 'https://tw.stock.yahoo.com/quote/2330.TW' #要爬的網站url
headers = {
    'User-Agent':'Mozilla/5.0'
} #避免讓網站知道是非人讀取,需要告訴網站這是從Mozilla/5.0進入,以免得到錯誤資訊或是被反爬蟲

res = requests.get(url,headers=headers) #對網址發送get請求

soup = BeautifulSoup(res.text,'html.parser') #使用解析器來將網站的HTML解析成類似xml的樹狀結構

stock_name = soup.find('h1',class_='C($c-link-text) Fw(b) Fz(24px) Mend(8px)')

stock_num = soup.find('span',class_='C($c-icon) Fz(24px) Mend(20px)')

price_tag = soup.find('span',class_='Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)')
#------以上三項為透過class標籤來擷取想要的結果------

now = datetime.now().strftime('%Y / %m / %d - %H：%M：%S') #時間戳記

#股票名 <h1 class="C($c-link-text) Fw(b) Fz(24px) Mend(8px)">台積電</h1>
#股票代號 <span class="C($c-icon) Fz(24px) Mend(20px)">2330</span>
#股價 <span class="Fz(32px) Fw(b) Lh(1) Mend(16px) D(f) Ai(c) C($c-trend-down)">972</span>
#股票HTML TAG資訊

if stock_name and stock_num and price_tag: #如果股票名字 代號 股價都找到資料的話(因為使用and連接所以缺一不可)
    print(f'於 {now} 擷取之 {stock_name.text}({stock_num.text}) 的當前股價為：{price_tag.text} 元台幣')
else:
    print('找不到該股票資訊')