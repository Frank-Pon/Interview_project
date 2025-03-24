from flask import Flask,Response,render_template
from GetStock import get_stock
import json

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stock/<stock_code>')
def stock_api(stock_code):
    result = get_stock(stock_code)
    json_str = json.dumps(result,ensure_ascii = False,indent = 2)
    return Response(json_str,content_type = "application/json; charset = utf-8")

if __name__ == '__main__':
    app.run(debug=True)