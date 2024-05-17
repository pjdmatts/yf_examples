import yfinance as yf
import sys
ticker = yf.Ticker("GE")
balance_df = ticker.balance_sheet
income_df = ticker.income_stmt
    
net_income = income_df.loc['Net Income', income_df.columns[0].strftime('%Y-%m-%d')]
shareholder_equity = balance_df.loc['Stockholders Equity', balance_df.columns[0].strftime('%Y-%m-%d')]
total_with_minority = balance_df.loc['Total Equity Gross Minority Interest', balance_df.columns[0].strftime('%Y-%m-%d')]

print("Net Income: ", f'{net_income:,}')
print("Shareholder Equity: ", f'{shareholder_equity:,}')
roe = net_income/shareholder_equity
print(float("{:.2f}".format(roe)))
print("Total Equity Gross Minority Interest: ", f'{total_with_minority:,}')
roe = net_income/total_with_minority
print(float("{:.2f}".format(roe)))