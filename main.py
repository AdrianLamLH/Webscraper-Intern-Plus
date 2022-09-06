import requests
from bs4 import BeautifulSoup

# Build for webmd
field = 'pediatrics'
state = 'California'
city = 'los-angeles'
End_Search = 0
URL = 'https://doctor.webmd.com/providers/specialty/'+field+'/'+state+'/'+city
print(URL)
page = requests.get(URL)
with open('out.txt', 'w') as f:
    print(page.content, file=f)
print(URL)
soup = BeautifulSoup(page.content, "html.parser")


user_table = soup.find_all('div', class_='results-card-wrap')
#while not End_Search: ignore for now (used for looping later on to check other pages of the search)
for user in user_table:
    user_links = (user.find_all('a')) # looks for all the a tags (happens to contain the user website, telephone num, and address)
    user_site = user_links[0].get('href')
    user_tele = user_links[len(user_links)-1].get('href')
    user_name = user.find('h2').get_text()
    user_spec = user.find('p', class_='prov-specialty').get_text()
    user_addr = user.find('span', class_='addr-text').get_text()
    print(user_name)
    print(user_spec)
    print(user_site)
    print(user_tele)
    print(user_addr)