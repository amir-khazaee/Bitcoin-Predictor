import datetime
import numpy
from requests import get
from bs4 import BeautifulSoup
from sklearn.linear_model import LinearRegression

# turns datetime object into unix seconds
def epoch_time(dt: datetime) -> int:
    return int((dt - datetime.datetime(1970, 1, 1)).total_seconds())

def generate_yahoo_csv_url(now: datetime) -> str:
    ten_days_ago = now - datetime.timedelta(days = 10)
    epoch_now = epoch_time(now)
    epoch_ten_days_ago = epoch_time(ten_days_ago)

    return f'https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1={epoch_ten_days_ago}&period2={epoch_now}&interval=1d&events=history&includeAdjustedClose=true'

# gives you a list of the last ten days' prices
# we'll be using the average of high and low, the 2nd and 3rd index respectively
def mine_data(csv_data: str) -> list:
    # gets the lines and reverses the order
    # it's a lazy fix to make sure we won't
    # accidentally try to parse the headers
    # as numbers
    lines = csv_data.split("\n")[::-1]

    last_ten_days = lines[0:10]
    averages = []

    for line in last_ten_days:
        nums = line.split(",")
        high = float(nums[2])
        low = float(nums[3])
        avg = (high + low) / 2
        averages.append(avg)
    
    return averages

# This header tricks the API into thinking we are a legit browser
header = headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = generate_yahoo_csv_url(datetime.datetime.now())

print("getting response from yahoo servers...")
resp = get(url, headers=header)
print("done.")

if not resp.ok:
    print("failed to fetch csv file. http status:", resp.status_code)
    exit()

csv_data = resp.text

# the current list is reversed, so 0th index
# is the current day, 1st is yesterday, etc...
# we reverse it again, so that the 0th day is
# ten days ago
# this makes the x labels make more sense
y_raw = mine_data(csv_data)[::-1]

# i got the whole prediction section from a
# tutorial, so I don't really know why we
# need to reshape x
x = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape((-1, 1))
y = numpy.array(y_raw)

print("training the model...")
lr = LinearRegression()
lr.fit(x, y)
print("done.")

prediction = lr.predict([[11]])[0]
print("prediction for price tomorrow:", prediction, "united states dollars")