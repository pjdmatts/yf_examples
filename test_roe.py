import yfinance as yf
import sys
ticker = yf.Ticker("GE")
balance_df = ticker.balance_sheet
income_df = ticker.income_stmt
    
net_income = income_df.loc['Net Income', income_df.columns[0].strftime('%Y-%m-%d')]
current_assets = balance_df.loc['Current Assets', balance_df.columns[0].strftime('%Y-%m-%d')]
current_liabilities = balance_df.loc['Current Liabilities', balance_df.columns[0].strftime('%Y-%m-%d')]
shareholder_equity = current_assets - current_liabilities

print(net_income)
print(shareholder_equity)

print("Balance Sheet: \n")

print(balance_df)