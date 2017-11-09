import requests
import csv,sys
from bs4 import BeautifulSoup


def writeFile(item):       
   with open('userID.csv', 'w') as t: 
     data = csv.writer(t,lineterminator='\n') 
     data.writerow(item)

with open('userURL.csv',newline='') as filecsv:
   reader = csv.reader(filecsv,delimiter='/')

   try:
       for row in reader:
           item = row[0].split('/')
           writeFile(item)
         #print(row)
   except csv.Error as e:
     sys.exit('file {}, line{}:{}'.format('userURL',reader.line_num,e))
