#Use Beautiful Soup package to show three different methods 

# (1/3) We will extract the price of the book "this is where it ends". 

import requests 
from bs4 import BeautifulSoup as bsoup

URL = "https://books.toscrape.com/catalogue/this-is-where-it-ends_771/index.html"
page = requests.get(URL)
soup = bsoup(page.text, "html.parser")

#find the price for the book "This is Where it Ends"

product = soup.find('div', class_='col-sm-6 product_main')
productprice = product.find('p', class_="price_color")

#get just the product price, not the whole selected line of HTML

if productprice:
    price = productprice.text
    print(f"The price of your book is {price}")
else: 
    print("Price not found. ")




# (2/3) Next, we will find how many copies of "This is Where it Ends" are available

product_availability = soup.find('th', string= 'Availability')
if product_availability:
    availability = product_availability.find_next('td').text
    print(availability)
else:
    print("Availability not found.")



# (3/3) Finally, we will pull the description of the book

description = soup.find('div', id= "product_description")
if description:
    product_description = description.find_next_sibling('p').text
    print(f"Description: {product_description}")
else:
    print("No description found")

