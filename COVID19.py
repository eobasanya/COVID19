#importing dependencies
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

#obtaining data
new_day = pd.read_csv("06-01-2020.csv")
historical_data = pd.read_csv("COVID19_Data")

#cleaning data
new_day = new_day[["Province_State", "Last_Update", "Confirmed", "Deaths","Recovered","Active", "Incident_Rate", "People_Tested", "People_Hospitalized", "Mortality_Rate", "Testing_Rate", "Hospitalization_Rate"]]
#current_date = datetime.date.today().strftime('%m/%d/%Y')
new_day[['Date', 'Time']] = new_day["Last_Update"].str.split(' ', expand=True)
new_day = new_day[["Date", "Confirmed", "Deaths","Recovered","Active", "Incident_Rate", "People_Tested", "People_Hospitalized", "Mortality_Rate", "Testing_Rate", "Hospitalization_Rate"]]
new_day = new_day.iloc[16:17]
historical_data = historical_data.append(new_day, ignore_index=True)


#Scatter Plot
#May3.plot.scatter(x="Province_State", y="Confirmed", c = "cyan")
#plt.rcParams.update({'font.size': 22})

#Line Plot - COVID Mortality Rate - Illinois
historical_data.set_index('Date')['Mortality_Rate'].plot(figsize=(100, 5), linewidth=0.7, color='maroon')
plt.xlabel("Date", labelpad=10)
plt.ylabel("Mortality_Rate", labelpad=10)
plt.title("COVID-19", y=1.02, fontsize=22)
plt.show()


#Line Plot: COVID-19 Deaths - Illinois
#plot1= historical_data.set_index('Date')['Deaths'].plot(figsize=(200, 5), linewidth=1.5, color='maroon')
#plt.xlabel("Date", labelpad=10)
#plt.ylabel("Deaths", labelpad=10)
#plt.title("COVID-19 Illinois", y=1.02, fontsize=22)
#plt.show()

#save updated historical data file
historical_data.to_csv("COVID19_Data.csv")
