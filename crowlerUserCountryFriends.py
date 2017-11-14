import requests, csv
from bs4 import BeautifulSoup
from collections import Counter

def writeFile (pk,pkFriend=" ", amigo=" "):
    with open('users_country_friends.csv', 'a') as f:
	    writeit = csv.writer(f, delimiter=',', lineterminator='\n')
	    if(amigo == " "):
	    	writeit.writerow([pk])
	    else:
	    	writeit.writerow([pk] + [pkFriend] + [amigo])

def findFriends(pk,country): 
	#for i in range (3):
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
                    countryFriend= row.find('span').get_text()
                    if(Counter(countryFriend)==Counter(country)):
                       writeFile(pk,pkFriend[6],1)
                    else:
                       writeFile(pk,pkFriend[6],0)
                    #print(url)
                    #print(country)
            #sem amigos                            
            else:
              writeFile(pk)                          
                                                          
with open('userPK.csv','r') as f:
	data = csv.reader(f, delimiter=',')
	for row in data:
		findFriends(row[0], row[1])		
    	   