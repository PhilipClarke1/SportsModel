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