import requests
import csv
from bs4 import BeautifulSoup

i=1

with open('userPK.csv', 'w',newline='') as f:
    writeit = csv.writer(f,delimiter=',')

    for i in range(1): 
        url = "http://www.englishbaby.com/findfriends/gallery/search?page="+ str(i) 
        r = requests.get(url)
        print (r.url, r.status_code)
        plain_text = r.text 

        soup = BeautifulSoup (plain_text, "html.parser")
        
        for li in soup.findAll ('li', {'class': 'super_member'}):            
              country= li.find('em').get_text()
              url = li.find_next('a').get('href')
              pk = url.split('/')
              writeit.writerow([pk[6]]+[country])
        

