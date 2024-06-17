import requests
from logo import Logo

TOKEN = "9fc1cdde8654b1b0d0253196b42c2158ebc1d0d9"

def get_link():
    LINK = input("Enter Link: ")
    return LINK

def shortener(LINK,TOKEN):
    response_data = {"long_url":LINK}
    header = {
    'Authorization': f'Bearer {TOKEN}'
    }
    response = requests.post(url="https://api-ssl.bitly.com/v4/shorten",headers=header,json=response_data)
    shorten_link = response.json()['link']
    return shorten_link
print(Logo)
LINK = get_link()
shorten_link = shortener(LINK=LINK,TOKEN=TOKEN)
print("Shorten Link: ",shorten_link)

