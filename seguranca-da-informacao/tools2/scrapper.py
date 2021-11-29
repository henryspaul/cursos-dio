from bs4 import BeautifulSoup
import requests
#import os

#os.chdir('D:\\MyProjects\\cursos-dio\\seguranca-da-informacao\\tools1')
'''
site = requests.get('https://www.ncbi.nlm.nih.gov/gene/85358').content
soup = BeautifulSoup(site,'html.parser')
print(soup.prettify())
'''
site = requests.get('https://www.ncbi.nlm.nih.gov').content
soup = BeautifulSoup(site,'html.parser')
temp = soup.find('span', class_='street-address')

print(temp.string)