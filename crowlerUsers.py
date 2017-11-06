import requests
import csv
#from random import randint


i=1

with open('userID.csv', 'w') as f:
    writeit = csv.writer(f, delimiter=',')

    for i in range(1,3): #[1,2[
        url = "http://www.englishbaby.com/findfriends/photos?page="+ str(i)
        r = requests.get(url)
        print (r.url, r.status_code)
        plain_text = r.text 

