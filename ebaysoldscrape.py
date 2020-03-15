import pandas as pd
from bs4 import BeautifulSoup
import requests


print("Enter eBay Search Term")
searchTerm = input()

print ("How many listings do you want saved? 25,50,100 or 200")
itemTotal = input()

itemUrl = ("https://www.ebay.com/sch/i.html?_from=R40&_nkw="+searchTerm+"&LH_Sold=1&_ipg="+itemTotal)
print (itemUrl)

page = requests.get(itemUrl) #requests html from url entered earlier
soup = BeautifulSoup(page.text, 'html.parser') #parses html file 
results = soup.find(id='srp-river-results')
items = results.find_all(class_='s-item__wrapper clearfix')

name = [item.find(class_='s-item__title s-item__title--has-tags').get_text() for item in items]
price = [item.find(class_='POSITIVE').get_text() for item in items]
shipping = [item.find(class_='s-item__shipping s-item__logisticsCost').get_text() for item in items]
endDate = [item.find(class_='s-item__ended-date s-item__endedDate').get_text() for item in items]

ebayListing = pd.DataFrame(
    {
        'Name': name,
        'Price': price,
        'Shipping': shipping,
        'End Date': endDate,
    })


print(ebayListing)

print('What would you like to name file?')
fileName = input()
ebayListing.to_csv(fileName+'.csv')