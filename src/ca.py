import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

#get current directory
currentDirectory = os.getcwd()

#read excel file
try:
    readxlsx = pd.read_excel(f"{currentDirectory}\Deaths.xlsx")

except FileNotFoundError as fne:
    print(f"File or directory not found  {fne.filename}")
    sys.exit()


#get the country index value
def CountryIndex(conName):
    index_value = readxlsx.index[readxlsx['country'] == conName].tolist()[0]
    return index_value
    

#get a specific value of any column based on the country index value      
def GetColumnValue(indexValue, columnName):
    value = readxlsx.iloc[indexValue][columnName]
    return float(value)
    

#Convert the first letter of each word in the input to upper-case
def CountryInputToUpper(entryTxt):
    toAList = entryTxt.split(" ")
    wordsToUpper = list(map(lambda words: words.capitalize(), toAList))
    toString = " ".join(wordsToUpper)
    return toString


def commands():
    print()
    print("COMMANDS MENU")
    print("ld   => To analyze covid deaths by country and gender")
    print("fv   => To analyze full vaccinations by country and gender")
    print("exit => Exit the program")
    print()


def AnalyzeDeathsByGender():
    


#function that plot the results in a bar chart
def PlotResults(maleDeaths, femaleDeaths, conName, totalDeaths):
    fig, ax = plt.subplots()

    gender      = ["Male", "Female"]
    count       = [maleDeaths, femaleDeaths]
    bars_label  = ["Male", "Female"]
    bars_colors = ['tab:blue', 'tab:pink']

    ax.bar(gender, count, label=bars_label, color=bars_colors, width=0.4)
    ax.set_ylabel("Total deaths in percentage %")
    ax.set_title(f"Total deaths in {conName} by gender {int(totalDeaths)}")
    ax.legend(title="Gender")
    plt.show()


countryInput = input("Insert a country name: ")
countryName  = CountryInputToUpper(countryInput)

try:

    index = CountryIndex(countryName)
    totalDeaths  = GetColumnValue(index, "total")
    maleDeaths   = GetColumnValue(index, "male")
    femaleDeaths = GetColumnValue(index, "female")
    
    print(f"{index} Total deaths:{int(totalDeaths)}  male:{maleDeaths}%  female:{femaleDeaths}%")

    PlotResults(maleDeaths, femaleDeaths, countryName, totalDeaths)

except (IndexError, NameError, TypeError):
    print("Incorrect country name please try again.")


def main():
    print("Covid analyzer")
    commands()

    while(True):
        command = input("Command: ").lower()

        if(command == "ld"):
