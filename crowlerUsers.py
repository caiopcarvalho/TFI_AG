import requests, csv
from random import randint
from bs4 import BeautifulSoup

i=1

with open('userID.csv', 'w') as f:
    writeit = csv.writer(f, delimiter=',')

    for i in range(1,3): #[1,2[
        url = "http://www.englishbaby.com/findfriends/gallery/detail/" + str(randint(1,2000))
        r = requests.get(url)
        print (r.url, r.status_code)
        plain_text = r.text 
