import pandas as pd
import matplotlib.pyplot as plt
from stock_data import *

data = pd.read_csv('stock-data.csv')

balance = 100
portfolio = {user_ticker: 0}

data['Short_MA'] = data['close'].rolling(window=50).mean()
data['Long_MA'] = data['close'].rolling(window=200).mean()
data['Signal'] = 0
data.loc[data['Short_MA'] > data['Long_MA'], 'Signal'] = 1
data.loc[data['Short_MA'] < data['Long_MA'], 'Signal'] = -1

for index, row in data.iterrows():
    if row['Signal'] == 1 and balance > 0:
        shares_to_buy = balance // row['close']
        portfolio[user_ticker] += shares_to_buy
        balance -= shares_to_buy * row['close']
    elif row['Signal'] == -1 and portfolio[user_ticker] > 0:
        shares_to_sell = portfolio[user_ticker]
        balance += shares_to_sell * row['close']
        portfolio[user_ticker] -= shares_to_sell

data['Portfolio Value'] = balance + portfolio[user_ticker] * data['close']

plt.plot(data['close'], label=f'{user_ticker} Close Price')
plt.plot(data['Short_MA'], label='50-day MA')
plt.plot(data['Long_MA'], label='200-day MA')
plt.title('Simulated Trading Strategy')
plt.legend()
plt.show()

plt.plot(data['Portfolio Value'], label='Portfolio Value', color='green')
plt.title('Simulated Portfolio Value Over Time')
plt.legend()

final_portfolio_value = data['Portfolio Value'].iloc[-1]
plt.text(data.index[-1], final_portfolio_value, f'${final_portfolio_value:.2f}', ha='right', va='bottom')

plt.show()