import yfinance as yf
import sys

# Function calculates Quick Ratio
def get_quick(ticker_in):
    ticker = yf.Ticker(ticker_in)
    balance_df = ticker.balance_sheet
    inventory = balance_df.loc['Inventory', balance_df.columns[0].strftime('%Y-%m-%d')]
    current_assets = balance_df.loc['Current Assets', balance_df.columns[0].strftime('%Y-%m-%d')]
    current_liabilities = balance_df.loc['Current Liabilities', balance_df.columns[0].strftime('%Y-%m-%d')]
    quick_ratio = (current_assets - inventory)/current_liabilities
    return float("{:.2f}".format(quick_ratio))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python quick_ratio_yf.py TICKER")
        sys.exit(1)

    ticker = sys.argv[1]
    current = get_quick(ticker)
    print("Quick: ", current)
