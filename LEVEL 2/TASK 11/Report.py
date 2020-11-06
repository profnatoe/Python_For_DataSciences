import pandas as pd
import numpy as np

#Read data from the file called 'balance.txt' into a DataFrame
balance = pd.read_csv('balance.txt', delim_whitespace = 1)#specify tha the delimiter is a single space


#compare average income based on ethnicity
ethnicity = balance.groupby("Ethnicity")

ethnicity_avg_income = ethnicity["Income"].agg(np.mean)
print(ethnicity_avg_income) 

#on average, do married or single people have a higher balance?

married_avg_income = balance.groupby('Married')["Balance"].mean()
print(married_avg_income)
married  = (balance.loc[balance['Married'] == 'Yes', 'Balance']).mean()
notMarried  = (balance.loc[balance['Married'] == 'No', 'Balance']).mean()

if married > notMarried:
    print("Married people have higher balance on Average than single people")
else:
    print("On Average single people have a higher balance than married people")


#Highest income
max_income = balance["Income"].max()
print(max_income)

#lowest income
min_income = balance["Income"].min()
print(min_income)

#how many cards do we have recorded in our dataset
cards_count = balance["Cards"].sum()
print(cards_count)


#How many females do we have information for vs how many males
gender_counts = balance["Gender"].value_counts(dropna=False)
print(gender_counts)



