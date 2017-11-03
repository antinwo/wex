import httplib2
import json
import operator
from functools import reduce


# from pprint import pprint


def get_from_dict(data_dict, map_list):
    return reduce(operator.getitem, map_list, data_dict)


def url(pair):
    symbol = 'https://wex.nz/api/3/ticker/' + pair
    return symbol


# print(url('btc_usd'))


http = httplib2.Http()
user_input = input("Please enter the symbol: ")
response, content = http.request(url(user_input), 'GET')
data = json.loads(content.decode('utf-8'))

#print(data)
print(get_from_dict(data, [user_input, "last"]))
