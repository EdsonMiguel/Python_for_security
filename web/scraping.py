from bs4 import BeautifulSoup
import requests

url = "https://github.com/EdsonMiguel"
site = requests.get(url).content
soup = BeautifulSoup(site, 'html.parser')
user_name = soup.find("span", class_="p-nickname vcard-username d-block")

print(user_name.string)
