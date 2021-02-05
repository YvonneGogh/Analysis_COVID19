#import libraries
import seaborn as sns
import pandas as pd 
import time
import numpy as np 
import matplotlib.pyplot as plt
print("All modules are imported")

#import datasets and show the first 5 rows
corona_dataset_csv=pd.read_csv("E:\Frank\covid19_project\\time_series_covid19_confirmed_global.csv")
print(corona_dataset_csv.head(5))

#know the shape of the dataframe
print(corona_dataset_csv.shape)

#delete useless columns
corona_dataset_csv.drop(["Lat","Long"],axis=1,inplace=True)
print(corona_dataset_csv.head(5))
print(corona_dataset_csv.shape)

#aggregating countries by rows
corona_dataset_aggregated = corona_dataset_csv.groupby("Country/Region").sum()
print(corona_dataset_aggregated.head(5))
print(corona_dataset_aggregated.shape)

#visualize data related to China and Italy
corona_dataset_aggregated.loc["China"].plot()
corona_dataset_aggregated.loc["Italy"].plot()
corona_dataset_aggregated.loc["Ireland"].plot()
plt.legend()
plt.show()

#changing time period
corona_dataset_aggregated.loc["China"][:3].plot()
plt.show()

#calculating the derivative of the curve
corona_dataset_aggregated.loc["China"].diff().plot()
plt.show()

#finding the maximum number of the derivative
print(corona_dataset_aggregated.loc["China"].diff().max())

#find maximum infenction rate for all countires
#and put them in a list
countries = list(corona_dataset_aggregated.index)
max_infection_rates = []
for c in countries:
    max_infection_rates.append(corona_dataset_aggregated.loc[c].diff().max())
print(max_infection_rates)

#put the above list into a new column
corona_dataset_aggregated["max_infection_rate"] = max_infection_rates
print(corona_dataset_aggregated.head())

#create a new dataframe that only shows the date
corona_date = pd.DataFrame(corona_dataset_aggregated["max_infection_rate"])
print(corona_date.head(5))


happiness_report=pd.read_csv("E:\Frank\covid19_project\worldwide_happiness_report.csv")
print(happiness_report.head(5))
print(happiness_report.shape)

#drop useless columns
useless_columns = ["Generosity","Score","Overall rank","Perceptions of corruption"]
happiness_report.drop(useless_columns,axis=1,inplace=True)
print(happiness_report.head(5))
print(happiness_report.shape)

happiness_report.set_index("Country or region",inplace=True)
print(happiness_report.head(5))

#join corona with happiness report
corona_dataset_aggregated.shape
data = corona_date.join(happiness_report,how="inner")

#correlation matrix
print(data.corr())

#visualize with seaborn
x = data["GDP per capita"]
y = data["max_infection_rate"]
sns.scatterplot(x,np.log(y))
plt.show()

sns.regplot(x,np.log(y))
plt.show()

