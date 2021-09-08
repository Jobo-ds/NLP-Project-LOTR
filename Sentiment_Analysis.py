## Imports
import pandas as pd
import plotly.express as px

## Data setup
data = pd.read_csv("lotrscript.csv")
data["char"] = data["char"].astype("category")
data["dialog"] = data["dialog"].astype("string")
data["movie"] = data["movie"].astype("category")
data = data.rename(columns={"char": "Character", "dialog": "Dialog", "movie": "Movie"})

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
remove_specialchars(data, "Dialog")

#Rename movie categories
data["Movie"] = data["Movie"].str.replace("Movie Script", "")

# There are some errors from data incorrectly entered in the CSV file. (See 2225 - 2238) - and a few misspelled names, voice overs and codenames.
data["Character"] = data["Character"].str.split(":", 1).str[0]
data["Character"] = data["Character"].str.replace("VOICE OVER", "")
data["Character"] = data["Character"].str.replace("VOICEOVER", "")
data["Character"] = data["Character"].str.replace("VOICE", "")
data["Character"] = data["Character"].str.replace("ARGORN", "ARAGORN")
data["Character"] = data["Character"].str.replace("GAN DALF", "GANDALF")
data["Character"] = data["Character"].str.replace("EYE OF SAURON", "SAURON") # Same character
data["Character"] = data["Character"].str.replace("STRIDER", "ARAGORN")

remove_specialchars(data, "Character")



## Data Analysis

# Comparing count of lines in each movie:
#fig01 = px.histogram(data, x="Movie")
#fig01.show()

#Comparing all characters count of lines:
fig01 = px.histogram(data, x="Character").update_xaxes(categoryorder='total descending')
fig01.show()
##

# Slimming dataframe to characters with more than 30 lines:
mainCharacter_count = data["Character"].value_counts()
mainCharacter = data[~data['Character'].isin(mainCharacter_count[mainCharacter_count < 30].index)]

fig01 = px.histogram(mainCharacter, x="Character").update_xaxes(categoryorder='total descending')
fig01.show()

##

