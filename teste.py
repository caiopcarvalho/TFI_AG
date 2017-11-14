import requests, csv

with open('userPK.csv', newline='') as f:
  reader =csv.reader(f, delimiter=',')
  for row in reader:
    print(row)