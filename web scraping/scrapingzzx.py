import requests
from bs4 import BeautifulSoup
url = "https://www.google.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print ("page title :", soup.title.text)
print ("Paragraph : ", soup.find('p').text)
# print ("Paragraph : ", soup.prettify())
