import requests
from bs4 import BeautifulSoup
url = "https://www.google.com/"

response = requests.get(url)
print( response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')
print ("page title :", soup.title.text)
print ("Paragraph : ", soup.find('p').text)
# print ("Paragraph : ", soup.prettify())
with open("index.html", "wb") as file:
    file.write(response.content)