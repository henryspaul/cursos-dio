from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.ncbi.nlm.nih.gov').content
soup = BeautifulSoup(site,'html.parser')
country = soup.find('span', class_='country-name')
print(soup.prettify())
print(country.string)
print(soup.title.string)