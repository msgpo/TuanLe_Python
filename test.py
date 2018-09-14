import requests
from bs4 import BeautifulSoup
import time
import csv
import re

#url ='https://www.sec.gov/Archives/edgar/data/1016538/0001016538-07-000015.txt'
url ='https://www.sec.gov/Archives/edgar/data/937886/0001193125-07-002711.txt'

#Read URL from the file
'''
with open('list.txt', 'r') as l:
    lines = l.readlines()
    url1 = lines[0]
    print url1
    '''
    
headers= {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url)
response.status_code
response.content

#Parsing to html format
soup = BeautifulSoup(response.content, 'html.parser')

#Find all table format <tabe></table>
stat_table =soup.find_all('table')
#Check how many table
len(stat_table)
#Select the first one
table = stat_table[0]

#Check table 

#for cell in table.find_all('c', limit = 1):
#    print(cell.text)
    
def main():
    #Create text file
    file = open('test.txt', 'w')
    #for row in table.find_all('s'):
    for cell in table.find_all('c', limit=1):
        file.write(cell.text.ljust(22))
        file.write('\n')
    file.close()
    #Open the text file (because table don't have readline(). I don't why, that's why stupid save and open lol)      
    textFile = open('test.txt', 'r')
    lines = textFile.readlines()
    print lines
    print len(lines)
    textFile.close()

#Process and save data to csv 

    mycsv = csv.writer(open('some.csv', 'w'))
    mycsv.writerow(['Name of Issuer','Title of class','CUSIP','Value', 'Share', 'SH', 'INVSTMT', 'SOLE','NONE'])
    for line in lines:
        print line
        if "COM" and "com" in line: #Should include more condition here
            name_of_issuer = line[0:36] #Should come up with better way to cover all cases
            print(name_of_issuer)
            title_of_class = line[37:41]
            print(title_of_class)
            cusip = line[43:52]
            print(cusip)
            value = line[53:58]
            print(value)
            share = line[61:68]
            print(share)
            sh = line[69:71]
            print(sh)
            invstmt = line[79:83]
            print(invstmt)
            sole = line[96:102]
            print(sole)
            none = line[110:116]
            print(none)
            mycsv.writerow([name_of_issuer, title_of_class, cusip, value, share, sh, invstmt, sole, none])


main()
