import requests
from bs4 import BeautifulSoup
import lxml
URL = "https://www.amazon.in/OnePlus-138-7-inches-Android-55U1S/dp/B095JQVC7N/ref=sr_1_3?crid=2F3CSUYGC0A9Q&keywords=oneplus+u1s+55+inch&qid=1666005845&qu=eyJxc2MiOiIxLjA5IiwicXNhIjoiMC4wMCIsInFzcCI6IjAuMDAifQ%3D%3D&sprefix=oneplus+u1s+55+inc%2Caps%2C215&sr=8-3"
header={
    "Accept-Language" : "en-US,en-IN;q=0.9,en;q=0.8m",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
}
response = requests.get(URL,headers=header)
website_html = response.text

soup = BeautifulSoup(website_html,"lxml")
price = soup.find("span", class_="a-offscreen")
print(price.getText().split("₹")[1])