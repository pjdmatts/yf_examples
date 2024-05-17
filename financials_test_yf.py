# Testing the yfinance library
# Leverage the Ticker module

import yfinance as yf

ticker = yf.Ticker("GE")

income_df = ticker.income_stmt
balance_df = ticker.balance_sheet
cash_df = ticker.cashflow

print("YFinance Income Statement\n")

print(income_df)

print("\nYFinance balance sheet\n")

print(balance_df)

print("\nYFinance cashflow\n")

print(cash_df)

