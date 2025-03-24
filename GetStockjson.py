from GetStock import get_stock
import json

search = input("請輸入股票代號：")
result = get_stock(search)

if result['status'] == 'Success':
    print(f"目前查詢的是股票代號 {search} 的 {result['stock_name']} ,此股票於 {result['time']} 的股價為 {result['stock_price']} 元{result['currency']}")
else:
    print(f'{result['status']}')

with open(f"{search}.json","w",encoding="utf-8") as f:
    json.dump(result,f,ensure_ascii=False,indent=2)