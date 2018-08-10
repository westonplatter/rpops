import requests

#
# rolling_mean_series
#

test_data = {"data": [1,2,1,2,1,2,1,2,1,2,1,2]}

# localhost
host = "18.217.49.2"

res = requests.post("http://{}:5000/rolling_mean_series".format(host), json=test_data)
result = res.json()
expected = {'errors': None, 'result': [None, None, None, None, None, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5]}
assert(result == expected)


# #
# # rolling_mean_df
# #
#
# test_data = {"data": [1,2,1,2,1,2,1,2,1,2,1,2]}
# res = requests.post('http://localhost:5000/rolling_mean_series', json=test_data)
# result = res.json()
# expected = {'errors': None, 'result': [None, None, None, None, None, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5]}
# assert(result == expected)
