import requests
from twilio.rest import Client 
account_sid = "AC1007642f283b0b51322868141f2ef45d"
auth_token  = "8639a38efcfd8a1f39829aca36b65826"

my_lat = 23.138639
my_lon = 72.536471
api_key = "74bcdf7e1bd33be6575e1060b8bcd0a5"
url = "https://api.openweathermap.org/data/2.5/weather"
rain_params = {
    "lat":my_lat,
    "lon":my_lon,
    "appid":api_key,
}
responses = requests.get(url,params=rain_params)
data = responses.json()['weather'][0]['main']
print(data)
client1 = Client(account_sid,auth_token)
message = client1.messages.create(
    to = '+919426380974',
    from_ = '+13862516407',
    body=f'''PYTHON SEND MESSAGE
    CURRENT WEATHER = "{data}"'''
)
print(message.sid)