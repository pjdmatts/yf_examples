import yfinance as yf
import sys

# Function calculates Return On Equity
def get_roe(ticker_in):
    ticker = yf.Ticker(ticker_in)
    balance_df = ticker.balance_sheet
    income_df = ticker.income_stmt
    net_income = income_df.loc['Net Income', income_df.columns[0].strftime('%Y-%m-%d')]
    shareholder_equity = balance_df.loc['Stockholders Equity', balance_df.columns[0].strftime('%Y-%m-%d')]
    roe = net_income/shareholder_equity
    return float("{:.2f}".format(roe))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python return_on_equity_yf.py TICKER")
        sys.exit(1)

    ticker = sys.argv[1]
    roe = get_roe(ticker)
    print("Retun On Equity: ", roe)