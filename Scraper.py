from bs4 import BeautifulSoup
import requests, re
url="https://xyz.com"
#url="https://www.usps.com/help/contact-us.htm"
page=requests.get(url)
soup=BeautifulSoup(page.content, "html.parser")
#print(soup.find_all("section-block pages bg-gray"))
p_element = soup.find(string=re.compile("[0-9]-([0-9]{3}-){2}[0-9{3,}", re.IGNORECASE))
print(p_element.parent.parent)
#ext=str(soup.prettify())
#rint(text)
#print(re.search("[pP][hH][Oo][nN][eE]",text))
#(re.search("[0-9]{3,}-[0-9]{5,}",text))
