import httplib2
import json
import operator
import time
from functools import reduce


def get_from_dict(data_dict, map_list):
    return reduce(operator.getitem, map_list, data_dict)


def url(pair):
    symbol = 'https://wex.nz/api/3/ticker/' + pair
    return symbol


pairs_url = 'https://wex.nz/api/3/info'

http = httplib2.Http()

pair_response, pair_content = http.request(pairs_url, 'GET')
pairs = json.loads(pair_content.decode('utf-8'))
print("Available pair list: ", list(pairs["pairs"].keys()))
print("Server time :", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(get_from_dict(pairs, ["server_time"]))))


user_input = input("Please enter pair symbol: ")
try:
    data_response, data_content = http.request(url(user_input), 'GET')
    data = json.loads(data_content.decode('utf-8'))

    print("High " + user_input + ": ", get_from_dict(data, [user_input, "high"]))
    print("Low " + user_input + ": ", get_from_dict(data, [user_input, "low"]))
    print("Last " + user_input + ":", get_from_dict(data, [user_input, "last"]))
    print("Updated :", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(get_from_dict(data, [user_input, "updated"]))))
except KeyError as key_err:
    print("There's no such pair: ", key_err)
