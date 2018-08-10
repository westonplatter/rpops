from flask import Flask, jsonify, request
import pandas as pd
import json
app = Flask(__name__)


@app.route('/rolling_mean_series', methods=['POST'])
def rolling_mean_series():
    j = request.json
    data = j["data"]

    window = (j["window"] if "window" in j else 6)

    # @TODO redo this so it's not serializing and deserializing
    mean = pd.Series(data).rolling(window=window).mean()
    json_values = mean.to_json(orient="values")
    array = json.loads(json_values)

    result = {"result": array, "errors": None}
    return jsonify(result)


@app.route("/")
def hello():
    """docstring"""
    return "Hello World!"


if __name__ == '__main__':
    app.run(host="0.0.0.0")
