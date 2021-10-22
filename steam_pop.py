import pandas as pd
import csv
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates
plt.style.use('seaborn')

data = pd.read_csv('steam_population/chart.csv')
data["DateTime"] = pd.to_datetime(data["DateTime"])
data.sort_values("DateTime", inplace=True)
date_time = data["DateTime"]
users = data["Users"]
in_game = data["In-Game"]
plt.plot_date(date_time, users, linestyle='solid', label = 'Users Online')
plt.plot_date(date_time, in_game, linestyle='solid', label = 'Users Online, In-Game')

plt.title('Steam Weekly Activities')
plt.xlabel('Date')
plt.ylabel('Online Popution (in Tens of Millions)')
plt.legend()
plt.show()