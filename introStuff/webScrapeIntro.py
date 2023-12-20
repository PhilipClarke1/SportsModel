import requests
from bs4 import BeautifulSoup
import pandas as pd 
import csv

player = 'Patrick Mahomes'
url = 'https://www.pro-football-reference.com/players/M/MahoPa00'
seasonYear = ['/gamelog/2021', '/gamelog/2022', '/gamelog/2023']

# add the season yr to the url 
r = requests.get(url + seasonYear[0])

soup = BeautifulSoup(r.text, 'html.parser')

season_table = soup.find('table', id="stats")

#with open('testgameData.csv', 'w') as f:

## open and write to testGameData.csv
f = open('testGameData.csv', 'w', newline='')
scrapedGames = csv.writer(f)

statList = []
headerCount = 0

for x in seasonYear:

    r = requests.get(url + x)

    soup = BeautifulSoup(r.text, 'html.parser')
    
    season_table = soup.find('table', id="stats")


    statList = []
    headerCount = 0
    ## html for tableheader 
    ## iterate through the headers and put the texts into a varaiable 
    for headers in season_table.find_all('th'):
        valueHeader = headers.text
        if valueHeader == 'Rk':
            headerCount = 1

        if headerCount == 1:
            statList.append(valueHeader)

    scrapedGames.writerow(statList)

    gameArray = []
    breakValue = 0
    for game in season_table.find_all('tr'):
        ## table data
        cols = game.find_all('td')
        statList = [player]
        for col in cols:
            if 'Upcoming' in col.text:
                breakValue = 1
                break
            else:
                stat_col = col.text
                statList.append(stat_col)
            if breakValue == 1:
                break 
        print (statList)
        scrapedGames.writerow(statList)
        gameArray.append(statList)  


