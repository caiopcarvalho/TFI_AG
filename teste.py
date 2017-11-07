from random import randint
#import requests

print("Olá mundo")
print("Git com vs")
print(randint(1,1999))

with open('userURL.csv','r') as filecsv:
   kkk = csv.reader(filecsv, delimiter='/')
         for row in reader:
          writeFile(row[0])

def writeFile(pk):
   with open('userID.csv', 'w') as f:
   data = csv.writer(f)
    data.writerow(pk);