#import the bs4 stuff --- use "uReq" and "soup"
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#assign any URL to be used....
#my_url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=-1&IsNodeId=1&Description=DJI&bop=And&PageSize=96&order=BESTMATCH'
my_url = 'https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&N=-1&IsNodeId=1&Description=DJI&bop=And&PageSize=12&order=BESTMATCH'

#opening connection, grab the page using "uReq"
uClient = uReq(my_url)
page_html = uClient.read()	#LOAD IT INTO "page_html" ---------- page_html is CREATED!!
uClient.close()

#use the "soup" function which is really just bs4
soup(page_html)

# do the html parsing into "page_soup"
page_soup = soup(page_html, "html.parser")

#body to span
page_soup.body.span

containerss = page_soup.findAll("div",{"class":"item-container"})

#should be 96
print("THIS IS THE LENGTH OF CONTAINERSS")
length = len(containerss)

print(length)

x = 0

for container in containerss:
	#brand = container.div.div.a.img["title"]
	
	title_container = container.findAll("a", {"class":"item-title"})
	title_container_name = title_container[0].text
	
	shipping_container = container.findAll("li", {"class":"price-was"})
	shippingCost = shipping_container[0].text.strip()

	#item_price = container.findAll("li", {"class":"price-current"})
	#item_price_num = item_price.text


	print("The Number On the Page:", x)
	#print("The Brand:" + brand)
	print("Product Name:" + title_container_name)
	#print("The OLD Price:" + shippingCost)

	#	print("The Price:" + item_price_num)

	x = x + 1














