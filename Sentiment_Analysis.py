## Imports
import pandas as pd
import plotly.express as px
import matplotlib

## Data setup
data_org = pd.read_csv("lotrscript.csv")
data = pd.read_csv("lotrscript.csv")

## Data Cleaning

# Function to remove special characters and some UTF formatting errors.
def remove_specialchars(dataframe, col):
    dataframe[col] = dataframe[col].str.replace("[^\w\s]", "")
    dataframe[col] = dataframe[col].str.replace("\n", "")
    dataframe[col] = dataframe[col].str.replace("\r", "")
    dataframe[col] = dataframe[col].str.replace("\xa0", "")
    for whitespace in range(0,5):
        j = ""
        j = j + " "
        dataframe[col] = dataframe[col].str.replace("  ", " ")
    dataframe[col] = dataframe[col].str.strip()

# Clean up "dialog" col
remove_specialchars(data, "dialog")

# There are some errors from data incorrectly entered in the CSV file. (See 2225 - 2238)
data["char"] = data["char"].str.split(":", 1).str[0]

remove_specialchars(data, "char")

# Make "movie" column categorical
data["movie"] = pd.factorize(data.movie)[0]


## Data Analysis

# Comparing lines in each movie:

# Count lines
i = data["movie"].value_counts()
i.plot(kind="bar")

#fig01 = px.bar(data, x="movie", y="")

