

import pandas as pd
from pandas_datareader import data, wb
import datetime


# We will look at stock prices over the past year, starting at January 1, 2016
start = datetime.datetime(2016,1,1)
end = datetime.date.today()

# input stock ticker symbol
# first argument is stock ticker, second is source, and then start and end date
apple = web.DataReader("AAPL", "yahoo", start, end)

type(apple)