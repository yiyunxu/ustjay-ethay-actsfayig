import requests
from bs4 import BeautifulSoup

response = requests.get("http://unkon.com")
#print(response.content)

soup = BeautifulSoup(response.content, "html.parser")
print(soup)
facts = soup.find_all("div", id="content")
#print(facts)
#print(facts[0].getText())
