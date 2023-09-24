import datetime
import requests

pixela_endpoint = "https://pixe.la/v1/users"
Token = "xsjkhfdakjhfhkghgfgh"
User = "shubham18072003"
graph_id = "graphrun"
pixela_params = {
    "token": Token,
    "username": User,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
graph_endpoint = f"https://pixe.la/v1/users/{User}/graphs"
graph_header = {
    "X-USER-TOKEN": Token,
}
graph_params = {
    "id":graph_id,
    "name":User,
    "unit":"km",
    "type":"float",
    "color":"sora",
}
# r = requests.post(url=graph_endpoint,json=graph_params,headers=graph_header)
# print(r.text)
value_endpoint = f"https://pixe.la/v1/users/{User}/graphs/{graph_id}"
today = datetime.datetime.now()
value_param={
    "date": today.strftime('%Y%m%d'),
    "quantity":input("Enter THe Distance You Run: "),
}
responses = requests.post(url=value_endpoint,json=value_param,headers=graph_header)
print(responses.text)