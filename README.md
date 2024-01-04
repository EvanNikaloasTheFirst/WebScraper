# WebScraper using Python ⏩

During my half term break I decided to spend 2 week learning more about Python and began using Codecademy and YouTube videos understanding they syntax.


I then build this web scraper application, I used:

- Python
- BeautifulSoup

## How it works

*The version is bespoke to the Gumtree website*

- The user input the login of the site they would like to scrape
 "https://www.gumtree.com/property-to-rent" <- this part is the generic domain of the site
 "/uk/hmo/page" <- Here are the Filter used in my search

/uk/ = I only wanted houses within the UK
/hmo/ = I wanted houses which had the term 'hmo' included in either the name or description
/page = This is the given page it would be scraping, using a variable that will be incremented, this allows my script to scrape multiple pages




The scripts creates a CSV File called 'hmos1.csv'
(Here is where all the details about the scraped data will go)

header = ['location','price','description','link'] = These are the specifc key words i'm looking for in the html source code.

so when my script is scaping the code it looks for the 4 headers, when the 4 items have been found it in a way conceptually uses it like an object and stores the corresponding details
and stores them into a line in the CSV file.

 When the script reaches  the end of the source code, the count variable is increased to move onto the next page (If it exists).
 
  
