import requests
from bs4 import BeautifulSoup
import rocketreach

def search_id(api_key, prof_link):
    r_r = rocketreach.Gateway(rocketreach.GatewayConfig('api-key'))
    result = r_r.person.lookup(linkedin_url=prof_link)
    print("email:",result.person)
# Build for linkedin

search_term = "site:linkedin.com/in/+AND+%22forensic+psychologist%22+AND+%22London%22"
page_number = 1
premium = ''
r_r_key = 
scraper_avoid = 'http://api.scraperapi.com?api_key=b70298e03167bf21aae54e352e49ab15&amp;url='
URL = scraper_avoid+'https://www.google.com/search?q=' + search_term + str(page_number) + premium
# URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)
with open('out.txt', 'w') as f:
    print(page.content, file=f)
print(URL)
soup = BeautifulSoup(page.content, "html.parser")


links = soup.find_all("a")
for link in links:
    link_url = link.get('href')
    if (("linkedin.com" in str(link_url)) and ("https://" in str(link_url))):
        name_tag = link.find('h3')
        name = name_tag.get_text()
        name = name.split(' -',1)[0]
        print(f"Full Name: {name}\n")
        search_id(r_r_key,str(link_url))
        print(f"Apply here: {link_url}\n")

# fp_list = soup.find_all("div", class_="entity-result")
# #print(page.text)
# for fp_profile in fp_list:
#     fp_page = fp_profile.find("a", class_="app-aware-link")
#     #print(fp_page)