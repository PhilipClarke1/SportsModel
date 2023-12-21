import nfl_data_py as nfl
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


pbp_data = nfl.import_pbp_data(years=[2023], columns=None, downcast=True, cache=False)

# Filter for New York Giants (assuming 'team' is the column for the team and 'posteam' is the offensive team)
# tenn_offense = pbp_data[(pbp_data['home_team'] == 'TEN')]
la_offense = pbp_data[(pbp_data['home_team'] == 'CIN')]

# Optionally, you can filter for specific types of offensive plays if you're interested in that
# For example, for passing plays: ny_giants_offense = ny_giants_offense[ny_giants_offense['play_type'] == 'pass']


# print(tenn_offense.head())
# print(tenn_offense.describe())

# tenn_offense.to_csv('tenn_offense_2021.csv', index=False)
la_offense.to_csv('la_offense_2023.csv', index=False)




# print(pbp_data)




Year = 2023
Team = 'MIA'


def get_team_offense_data(year, team):
    # Import play-by-play data for the specified year
    pbp_data = nfl.import_pbp_data(years=[year], columns=None, downcast=True, cache=False)

    # Filter data for the specified team
    team_offense = pbp_data[(pbp_data['home_team'] == team)]

    # Save the filtered data to a CSV file
    csv_filename = f'{team}_offense_{year}.csv'
    team_offense.to_csv(csv_filename, index=False)

    # Select specific columns if they exist in the DataFrame
    desired_columns = ['column1', 'column2', 'column3']  # Replace with actual column names
    team_offense = team_offense[desired_columns] if all(col in team_offense.columns for col in desired_columns) else team_offense

    # Convert the filtered data to a DataFrame if it's not already
    if not isinstance(team_offense, pd.DataFrame):
        team_offense = pd.DataFrame(team_offense)
    
    
    df=pd.DataFrame(team_offense)
    return df