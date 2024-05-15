import yfinance as yf
import sys

def get_current(ticker_in):
    ticker = yf.Ticker(ticker_in)
    balance_df = ticker.balance_sheet
    current_assets = balance_df.loc['Current Assets', balance_df.columns[0].strftime('%Y-%m-%d')]
    current_liabilities = balance_df.loc['Current Liabilities', balance_df.columns[0].strftime('%Y-%m-%d')]
    current_ratio = current_assets/current_liabilities
    return float("{:.2f}".format(current_ratio))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python finutils_driver.py TICKER")
        sys.exit(1)

    ticker = sys.argv[1]
    current = get_current(ticker)
    print("Current: ", current)

