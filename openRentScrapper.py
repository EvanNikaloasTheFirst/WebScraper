from bs4 import BeautifulSoup
# pip3 install requests
import requests
from csv import writer

url= "https://www.openrent.co.uk/properties-to-rent/birmingham-west-midlands?term=Birmingham,%20West%20Midlands&prices_min=1000&prices_max=2870&bedrooms_min=3&bedrooms_max=7"

page = requests.get(url)

properties = BeautifulSoup(page.content,'html.parser')
lists = properties.find_all('a', class_="pli clearfix")

with open('house1.csv','w', encoding='utf8', newline='')as f:
    thewriter = writer(f)
    header = ['location','price','description','link']
    thewriter.writerow(header)
    for list in lists:
        location = list.find('span', class_="banda pt listing-title").text.replace('\n','')
        price = list.find('h2', class_="").text.replace('\n','')
        description = list.find('p', class_="listing-desc").text.replace('\n','')
        link = list.get('href')
        activeLink = "https://www.openrent.co.uk" + link
        info = [location,price,description,activeLink]
        thewriter.writerow(info)


# banda pt listing-title
# https://www.openrent.co.uk