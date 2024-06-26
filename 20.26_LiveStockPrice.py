# Get Live Stock Price Data using Python and place it to any of your web application.
# Open Yahoo Finance on your Browser.
import yfinance as yf
from datetime import date, timedelta
today = date.today()
d1 = today.strftime("%Y-%m-%d")
end_date = d1
d2 = date.today() - timedelta(days=360)
d2.strftime("%Y-%m-%d")
start_date = d2
data = yf.download("AAPL", start=start_date, end=end_date, progress=False)
# print(data)
data["Date"] = data.index
data = data[["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"]]
data.reset_index(drop=True, inplace=True)
print(data.head())