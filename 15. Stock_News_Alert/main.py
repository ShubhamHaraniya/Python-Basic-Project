from datetime import datetime
import datetime as dt
import calendar
import requests
from twilio.rest import Client
account_sid = "AC1007642f283b0b51322868141f2ef45d"
auth_token  = "8639a38efcfd8a1f39829aca36b65826"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_key =  "HHM8UXDJ2M5Q7F6M"
url_link = 'https://www.alphavantage.co/query'
url_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : api_key,
}

response = requests.get(url=url_link,params=url_params)

today = str(datetime.now()).split(" ")[0]
yesterday =today.replace(today.split("-")[2],str(int(today.split("-")[2])-1))
Day_Before = today.replace(today.split("-")[2],str(int(today.split("-")[2])-2))

Holiday_days = ['sunday','saturday']
def findDay(date):
    day = dt.datetime.strptime(date, '%Y-%m-%d').weekday()
    return (calendar.day_name[day]).lower()

while findDay(yesterday) in Holiday_days:
    yesterday = yesterday.replace(yesterday.split("-")[2],str(int(yesterday.split("-")[2])-1))
while findDay(Day_Before) in Holiday_days or yesterday == Day_Before:
    Day_Before = Day_Before.replace(Day_Before.split("-")[2],str(int(Day_Before.split("-")[2])-1))
data_yesterday = response.json()['Time Series (Daily)'][yesterday]['4. close']
data_day_before = response.json()['Time Series (Daily)'][Day_Before]['4. close']



client = Client(account_sid, auth_token)




if data_yesterday < data_day_before:
    message = client.messages.create(
    to="+919426380974", 
    from_="+13862516407",
    body=f'''Stock Value Goes Down
    On {yesterday} it is {data_yesterday} USD
    On {Day_Before} it is {data_day_before} USD''')
    print(message.sid)
if data_yesterday > data_day_before:
    message = client.messages.create(
    to="+919426380974", 
    from_="+13862516407",
    body=f'''Stock Value Goes Down
    On {yesterday} it is {data_yesterday} USD
    On {Day_Before} it is {data_day_before} USD''')
    print(message.sid)
if data_yesterday == data_day_before:
    message = client.messages.create(
    to="+919426380974", 
    from_="+13862516407",
    body=f'''Stock Value Goes Down
    On {yesterday} it is {data_yesterday} USD
    On {Day_Before} it is {data_day_before} USD''')
    print(message.sid)