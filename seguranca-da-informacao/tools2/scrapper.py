from bs4 import BeautifulSoup
import requests
'''
site = requests.get('https://www.ncbi.nlm.nih.gov/gene/85358').content
soup = BeautifulSoup(site,'html.parser')
print(soup.prettify())
'''
site = requests.get('https://www.ncbi.nlm.nih.gov').content
soup = BeautifulSoup(site,'html.parser')
#temp = soup.find('span', class_='_block _margin-b-5 -gray')

print(soup.prettify())
