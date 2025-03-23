from GetStock import get_stock


search = input("請輸入股票代號：")
result = get_stock(search)

if result['status'] == 'Success':
    print(f"目前查詢的是股票代號 {search} 的 {result['stock_name']} ,此股票於 {result['time']} 的股價為 {result['stock_price']} 元{result['currency']}")
else:
    print(f'{result['status']}')