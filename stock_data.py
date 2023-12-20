from polygon import RESTClient
import csv

client = RESTClient(api_key="P5lD5kAdAAPWKhVCUpBWy5X13uCWaPk9")
user_ticker = input("Insert the stock ticker you want to see the data for. Make sure you use capital letters and the ticker is right: ")
ticker = user_ticker

from_time = input("Please insert the date from which you want to recieve data as (yyyy-mm-dd): ")
to_time = input("Please insert the date to which you want to receive data as (yyyy-mm-dd): ")
from_day = int(from_time[-3:-1])
to_day = int(to_time[-3:-1])

aggs = []
for a in client.list_aggs(ticker=user_ticker, multiplier=1, timespan="minute",
                            from_=from_time, to=to_time, limit=50000):
    aggs.append(a)

data_list = []
for i in range(len(aggs)):
    day_dict = aggs[i].__dict__
    data_list.append([day_dict['open'], day_dict['high'], day_dict['low'], day_dict['close'], day_dict['volume']])

fields = ['open', 'high', 'low', 'close', 'volume']

with open("stock-data.csv", 'w') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(fields)
    csv_writer.writerows(data_list)

