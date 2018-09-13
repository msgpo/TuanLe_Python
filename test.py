import requests
from bs4 import BeautifulSoup
import time

url ='https://www.sec.gov/Archives/edgar/data/937886/0001193125-07-002711.txt'


headers= {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url)
response.status_code
response.content

#Parsing to html format
soup = BeautifulSoup(response.content, 'html.parser')

#Find all table format <tabe></table>
stat_table =soup.find_all('table')
#Check how many table
#Select the first one
table = stat_table[0]

#Check table have column <s></s> (Name of Issuer)
#Check column <c></c> (Data)
#Print column
for row in table.find_all('s'):
    for cell in row.find_all('c'):
        print(cell.text)
        
#Create text file
with open ('test.txt', 'w') as r:
    for row in table.find_all('s'):
        for cell in row.find_all('c'):
            r.write(cell.text.ljust(22))
        r.write('\n')
        

