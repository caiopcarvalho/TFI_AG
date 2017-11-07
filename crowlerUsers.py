import requests
import csv
from bs4 import BeautifulSoup
#from random import randint

def writeFile(item):
       
   with open('userID.csv', 'a') as t: 
     data = csv.writer(t) 
     data.writerow(item)

i=1

with open('userURL.csv', 'w') as f:
    writeit = csv.writer(f, delimiter=',')

    for i in range(1,4): #[1,2[
        url = "http://www.englishbaby.com/findfriends/gallery/search?page="+ str(i) 
        r = requests.get(url)
        print (r.url, r.status_code)
        plain_text = r.text 

        soup = BeautifulSoup (plain_text, "html.parser")
        
        for li in soup.findAll ('li', {'class': 'super_member'}):
            link = li.find_next('a').get('href')
            writeit.writerow([link])

with open('userURL.csv','r') as filecsv:
   reader = csv.reader(filecsv, delimiter='/')

   for row in reader:
      item = row[6]
      writeFile(item)

