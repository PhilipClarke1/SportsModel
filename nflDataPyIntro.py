import nfl_data_py as nfl
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def filter_team_pbp_to_csv(team_abbr, year):
    
    # Import play-by-play data for the specified year
    pbp_data = nfl.import_pbp_data(years=[year], columns=None, downcast=True, cache=False)
    
    # Filter for the specified team
    team_data = pbp_data[(pbp_data['home_team'] == team_abbr) | (pbp_data['away_team'] == team_abbr)]
    
    # Save the filtered data to a CSV file
    filename = f'{team_abbr.lower()}_offense_{year}.csv'
    team_data.to_csv(filename, index=False)
    print(f"Data for {team_abbr} in {year} has been saved to {filename}")


filter_team_pbp_to_csv('CIN', 2023)