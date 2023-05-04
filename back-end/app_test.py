from flask import Flask, jsonify
import random
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

cors = CORS(app)

sensor_list = [
    "温度",
    "湿度",
    "压力",
    "流量",
    "液位",
    "电流",
    "电压",
    "震动",
    "光照",
    "二氧化碳",
    "甲醛",
    "转速",
    "红外温度",
    "压力变送",
    "液位变送",
    "二氧化硫",
    "氨气",
    "甲烷",
    "一氧化碳",
    "含氧量",
    "PH传感器",
    "渗透压"
    "粉尘"
]

n = 50

@app.route('/data', methods=['GET'])
def get_data():
    xData = [i for i in range(1, n)]
    x = random.randint(1, 100)
    yData = [random.randint(1, n)+x for i in range(1, n)]
    data = {
        'x_data': xData,
        'y_data': yData,
        'title': random.choice(sensor_list)
    }
    res = jsonify(data)
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res

if __name__ == '__main__':
    app.run(debug=True)