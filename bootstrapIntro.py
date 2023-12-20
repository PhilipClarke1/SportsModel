import random 
from random import randrange
import pandas as pd
import numpy as np
import csv

##### get WNBA data csv and run it with this code 

f = open('testing WNBA results.csv', 'w', newline='')
testOutput = csv.writer(f)

# load in the data files 
playerSeasonData = pd.read_csv("WNBA Seasonal Stats New.csv")
playerSelectedData = pd.read_csv('WNBA Game Lineups.csv')

# Set home defense
home_defense_selected = playerSelectedData['Home Defense'].iloc[2]

# Set away defense
away_defense_selected = playerSelectedData['Away Defense'].iloc[2]

def game_simulation(basketball_team):
    for g in range(0,1):
        player_2p_acc_list = []
        final_2p_acc_list = []
        # grab the first person on the away team "name" and this is the data that matches that name
        playerSelected = playerSelectedData[basketball_team].iloc[g]
        # locate the rows of data to be used 
        player_advanced_row = playerSeasonData.loc[(playerSeasonData["Rk"]  == playerSelected)]
        numSelect = int(player_advanced_row[player_advanced_row.columns[0]].count())
        # print(numSelect)
        for y in range(0,1000):
            for xx in range(0,100):
                rRecord = randrange(numSelect)
                player_2p_acc_list.append(player_advanced_row["2p%"].iloc[rRecord])
            final_2p_acc_list.append(np.mean(player_2p_acc_list))
        print(np.mean(final_2p_acc_list))



n = 'Away Player'
game_simulation(n)