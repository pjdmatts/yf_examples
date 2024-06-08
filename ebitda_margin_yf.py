import yfinance as yf
import sys

# Function calculates EBITDA Margin
def get_ebitda_margin(ticker_in):
    ticker = yf.Ticker(ticker_in)
    income_df = ticker.income_stmt
    ebitda = income_df.loc['EBITDA', income_df.columns[0].strftime('%Y-%m-%d')]
    revenue = income_df.loc['Total Revenue', income_df.columns[0].strftime('%Y-%m-%d')]
    ebitda_margin = ebitda/revenue
    return float("{:.2f}".format(ebitda_margin))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ebitda_margin_yf.py TICKER")
        sys.exit(1)

    ticker = sys.argv[1]
    ebitda_margin = get_ebitda_margin(ticker)
    print("EBITDA Margin: ", ebitda_margin)