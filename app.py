from flask import Flask, jsonify, request
import pandas as pd
import json
app = Flask(__name__)

@app.route('/rolling_mean_series', methods=['POST'])
def rolling_mean_series():
    j = request.json
    data = j["data"]

    if "window" in j:
        window = j["window"]
    else:
        window = 6

    # @TODO redo this so it's not serializing and deserializing
    mean = pd.Series(data).rolling(window=window).mean()
    json_values = mean.to_json(orient="values")
    array = json.loads(json_values)

    result = {
        "result": array,
        "errors": None }

    return jsonify(result)
