import pandas as pd

# This function is used to load a data csv file 
data = pd.read_csv('01.Data Cleaning and Preprocessing.csv')

type(data)


data

#This function is used to display the first N rows of a DataFrame 
data.head(2)


# This function is used to display the last N rows of a DataFrame 
data.tail(2)


# This function is used to generate summary statistics of a DataFrame's
data.describe()


# The below line filters the DataFrame 
filtered_data = data[data['ChipRate'] < 10.0]
filtered_data


data.isnull()


# This function returns a Series that shows the total number of null values in each coloumn
data.isnull().sum()


# This function returns the total number of null values in entire DataFrame 
data.isnull().sum().sum()


# This function is used to replace all null vales in the DataFrame
second_DataFrame = data.fillna(value=0) 
second_DataFrame


# This function is used to remove duplicaates rows from the DataFrame
data = data.drop_duplicates()
data
