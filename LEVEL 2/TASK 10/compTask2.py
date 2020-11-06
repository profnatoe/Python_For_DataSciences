import numpy as np
import pandas as pd

#Read data from the file called 'credit.csv' into a DataFrame
credit = pd.read_csv('credit.csv',
                            delim_whitespace = 1)#specify tha the delimiter is a single space


#prints the first 10 rows of the dataframe
print(credit.head(10))

#print the age and education columns
ageEducation = credit.iloc[0:,[2,3]]
print(ageEducation)


#print users who are above the age of 30 
ageAbove30 = credit[credit.Age > 30]
print(ageAbove30)