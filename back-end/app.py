from flask import Flask, jsonify
import pandas as pd
import random
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(__name__)

cors = CORS(app)

df = pd.read_csv('./data/processed/70_batch_pred_merged.csv') 

df_batch = dict(list(df.groupby('Batch_ref')))

new_dict = {}
count = 0

def split_intervals_and_points(input_list):
    input_list = sorted(set(input_list))
    intervals = []
    points = []
    
    i = 0
    while i < len(input_list):
        if i + 1 < len(input_list) and input_list[i + 1] - input_list[i] == 1:
            start = input_list[i]
            while i + 1 < len(input_list) and input_list[i + 1] - input_list[i] == 1:
                i += 1
            end = input_list[i]
            intervals.append((start, end))
            points.append(start)
            points.append(end)
        else:
            points.append(input_list[i])
        i += 1
    
    return intervals, points

for k, v in df_batch.items():
    new_dict[count] = v.to_dict('list')
    if 'prediction_for_next' in new_dict[count].keys():
        del new_dict[count]['prediction_for_next']
    if 'abnormal_detection' in new_dict[count].keys():
        new_dict[count]['abnormal_detection'] = [
            i for i, x in enumerate(new_dict[count]['abnormal_detection']) if x == 1]
    if 'normal' not in new_dict[count].keys():
        if len(new_dict[count]['abnormal_detection'])>0:
            new_dict[count]['normal'] = False
        else:
            new_dict[count]['normal'] = True
    new_dict[count]['markArea'], new_dict[count]['markLine'] = split_intervals_and_points(new_dict[count]['abnormal_detection'])
    del new_dict[count]['abnormal_detection']
    count += 1
    
app = Flask(__name__)

@app.route('/api/data/<int:n>', methods=['GET'])
def generate_data(n):
    res = jsonify(new_dict[n])
    res.headers.add('Access-Control-Allow-Origin', '*')
    return res

if __name__ == '__main__':
    app.run(debug=True)