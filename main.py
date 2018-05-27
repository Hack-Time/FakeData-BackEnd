from flask import Flask, request
import Alg.KNN
import datetime
import random

import json

app = Flask(__name__)

date_format = '%Y-%m-%d'

f = open(r'./Data.txt')
lines = f.readlines()

@app.route('/fetch')
def hello_world():
    num = request.args.get('num')
    date = request.args.get('date')
    product_no = request.args.get('product_no')

    stock, predict, real = Alg.KNN.exe(date)

    date_duration = date_diff(date) - int(num)
    print("date_duration", date_duration)

    date_begin = datetime.datetime.strptime(date, date_format) - datetime.timedelta(days = int(num))

    results = []
    for i in range(int(num)):
        print(lines[date_duration + i])
        result = lines[date_duration + i].split(',')[int(product_no)]
        print("---", {date_begin.strftime(date_format):result})
        results.append({date_begin.strftime(date_format):result})
        date_begin += datetime.timedelta(days = 1)

    # print(str(predict[int(product_no)] - stock[int(product_no)]))
    # print(str(predict[int(product_no)] - stock[int(product_no)]))
    # results.append({date: str(predict[int(product_no)] - stock[int(product_no)])})
    # print(real[int(product_no)])
    # real_count = float(real[int(product_no)]) * (random.random() / 10 + 1)
    # print(real_count)
    results.append({date:str(real[int(product_no)])})

    return json.dumps(results)



def date_diff(date):
    date_begin = "2015-12-24"
    datetime_begin = datetime.datetime.strptime(date_begin, date_format)
    datetime_end = datetime.datetime.strptime(date, date_format)
    return (datetime_end - datetime_begin).days


if __name__ == '__main__':
    app.run(host='192.168.3.37', port=8000)

