# Total Debt / Total Assets

import yfinance as yf
import sys

# Function calculates Debt To Assets
def get_dta(ticker_in):
    ticker = yf.Ticker(ticker_in)
    balance_df = ticker.balance_sheet
    total_debt = balance_df.loc['Total Debt', balance_df.columns[0].strftime('%Y-%m-%d')]
    total_assets = balance_df.loc['Total Assets', balance_df.columns[0].strftime('%Y-%m-%d')]
    dta = total_debt/total_assets
    return float("{:.2f}".format(dta))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python debt_to_assets_yf.py TICKER")
        sys.exit(1)

    ticker = sys.argv[1]
    dta = get_dta(ticker)
    print("Retun On Assets: ", dta)