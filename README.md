⭐股票查詢side project

簡介:

這是一支股票資料查詢程式,只要輸入台灣股票代號,就能將查詢的資料透過API儲存成json檔,並透過整合前端來將查詢結果作呈現

功能使用說明:

User 輸入股票代號 (例:2330 ,就可以查詢到台積電)
透過程式爬取Yahoo股市的資料來找到輸入代號的股票
將結果以API的方式回傳成json檔
接著透過HTML及JS即時呈現
另外,也有基本的錯誤提示訊息

✔️python 3.12
✔️Flask
✔️Requests
✔️BeautifulSoup
✔️json
✔️HTML/JavaScript

使用方法:

(https://github.com/Frank-Pon/Interview_project.git) clone之後 -> 安裝所需套件 ( Flask、Requests、BeautifulSoup )
-> 在終端機輸入 python app.py -> 打開網頁輸入 127.0.0.1:5000 -> 開始查詢 ✅

![畫面截圖](screenshot/app.png)
![畫面截圖](screenshot/index.png)
![畫面截圖](screenshot/web.png)
![畫面截圖](screenshot/search.png)
![畫面截圖](screenshot/search_failed.png)


