import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

#url = 'https://www.pro-football-reference.com/teams/'+x+'/2022_roster.htm'
url = 'https://www.pro-football-reference.com/years/2022/passing_advanced.htm'
print(url)

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
soup2 = BeautifulSoup(r.content, 'html.parser')

player_table = soup2.find('table', id = 'advanced_air_yards')

print(player_table)
