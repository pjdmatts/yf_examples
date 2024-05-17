import yfinance as yf
import sys

# Function calculates Net Profit Margin
def get_profit_margin(ticker_in):
    ticker = yf.Ticker(ticker_in)
    income_df = ticker.income_stmt
    net_profit = income_df.loc['Net Income', income_df.columns[0].strftime('%Y-%m-%d')]
    revenue = income_df.loc['Total Revenue', income_df.columns[0].strftime('%Y-%m-%d')]
    profit_margin = net_profit/revenue
    return float("{:.2f}".format(profit_margin))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python net_profit.py TICKER")
        sys.exit(1)

    ticker = sys.argv[1]
    profit = get_profit_margin(ticker)
    print("Net Profit Margin: ", profit)