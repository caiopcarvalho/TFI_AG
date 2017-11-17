import requests, csv
from bs4 import BeautifulSoup
from collections import Counter

def writeFile (pk,pkFriend=" "):
    with open('users_friends20.csv', 'a') as f:
	    writeit = csv.writer(f, delimiter=',', lineterminator='\n')
	    if(pkFriend == " "):
	    	writeit.writerow([pk])
	    else:
	    	writeit.writerow([pk] + [pkFriend])

def findFriends(pk): 
    url ="http://www.englishbaby.com/findfriends/gallery/detail/"+pk
    r=requests.get(url)
    print(r.url,r.status_code)
    plain_text=r.text
    soup=BeautifulSoup (plain_text, "html.parser")
    
    if(r.status_code==200):
        for body in soup.find_all('body',{'id':'free_member'}):
            #encontra usuário com amigos
            if(body.find('table',{'class': 'lesson_grid lesson_grid_members'})):
                table = soup.find('table',{'class': 'lesson_grid lesson_grid_members'})
                for row in table.find_all('td'):
                    url = row.find_next('a').get('href')
                    pkFriend = url.split('/')
                    writeFile(pk,pkFriend[6])
                    print(pkFriend[6])
                                                  
            else:
              writeFile(pk)                          
                                                          
with open('userPK1.csv','r') as f:
	data = csv.reader(f, delimiter=',')
	for row in data:
		findFriends(row[0])		
    	   