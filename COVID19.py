import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

new_day = pd.read_csv("06-01-2020.csv")
historical_data = pd.read_csv("COVID19_Data")

new_day = new_day[["Province_State", "Confirmed", "Deaths","Recovered", "People_Tested", "People_Hospitalized", "Mortality_Rate", "Testing_Rate", "Hospitalization_Rate"]]
new_day = new_day.iloc[19]
historical_data.append(new_day)


#Scatter Plot
#May3.plot.scatter(x="Province_State", y="Confirmed", c = "cyan")
#plt.rcParams.update({'font.size': 22})

#Line Plot
historical_data.set_index('Province_State')['Deaths'].plot(figsize=(200, 5), linewidth=1.5, color='maroon')
plt.xlabel("State", labelpad=10)
plt.ylabel("Deaths", labelpad=10)
plt.title("COVID-19 Deaths", y=1.02, fontsize=22)
plt.show()
#save updated historical data file
historical_data.to_csv("COVID19_Data.csv")
