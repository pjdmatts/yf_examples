import yfinance as yf
import sys

# Function calculates Return On Assets
def get_roa(ticker_in):
    ticker = yf.Ticker(ticker_in)
    balance_df = ticker.balance_sheet
    income_df = ticker.income_stmt
    net_income = income_df.loc['Net Income', income_df.columns[0].strftime('%Y-%m-%d')]
    total_assets = balance_df.loc['Total Assets', balance_df.columns[0].strftime('%Y-%m-%d')]
    roa = net_income/total_assets
    return float("{:.2f}".format(roa))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python return_on_assets_yf.py TICKER")
        sys.exit(1)

    ticker = sys.argv[1]
    roa = get_roa(ticker)
    print("Retun On Equity: ", roa)