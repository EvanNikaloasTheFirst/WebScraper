from bs4 import BeautifulSoup
import requests
from csv import writer
import validators

count = 1
url = "https://www.gumtree.com/property-to-rent/uk/hmo/page"

with open('hmos1.csv','w', encoding='utf8', newline='')as f:
    thewriter = writer(f)
    header = ['location','price','description','link']
    thewriter.writerow(header)
    while(True):
        current_url = url + str(count)
        if not validators.url(current_url):
            break
        page = requests.get(current_url)
        if page.status_code != 200:
            break
        properties = BeautifulSoup(page.content,'html.parser')
        lists = properties.find_all('a', class_="listing-link")

        for list in lists:
            location = list.find('h2', class_="listing-title").text.replace('\n','')
            price = list.find('strong', class_="h3-responsive").text.replace('\n','')
            description = list.find('p', class_="listing-description txt-sub txt-tertiary truncate-paragraph hide-fully-to-m").text.replace('\n','')
            link = list.get('href')

            info = [location,price,description,link]
            thewriter.writerow(info)
        count+=1
