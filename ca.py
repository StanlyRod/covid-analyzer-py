
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


#get the country index value of the excel file
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


#display all the commands
def commands():
    print()
    print("COMMANDS MENU")
    print("ld   - To analyze covid deaths by country and gender")
    print("fv   - To analyze full vaccinations by country and gender")
    print("cmd  - To list all the commands available")
    print("exit - Exit the program")
    print()



#function that plot the results in a bar chart
def PlotDeathsResults(maleDeaths, femaleDeaths, conName, totalDeaths):
    fig, ax = plt.subplots()
    ax.set_facecolor('gray')   #ax in gray color
    fig.set_facecolor("black") #fig in black color
    
    gender      = ["Male", "Female"]
    count       = [maleDeaths, femaleDeaths]
    bars_label  = [f"Male {round(maleDeaths)}%", f"Female {round(femaleDeaths)}%"]
    bars_colors = ['tab:purple', 'tab:pink']

    ax.bar(gender, count, label=bars_label, color=bars_colors, width=0.4)
    ax.set_ylabel("Total deaths in percentage %", color='white')
    ax.set_title(f"Total deaths in {conName} by gender {int(totalDeaths)}", color='white')
    ax.legend(title="Gender")

    #set frame width 
    ax.spines['bottom'].set_linewidth(3)
    ax.spines['top'].set_linewidth(3)
    ax.spines['left'].set_linewidth(3)
    ax.spines['right'].set_linewidth(3)
 
    #set frame color
    ax.spines['bottom'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')

    ax.tick_params(labelcolor='orange')
    plt.show()


#display the death final results
def DeathResults():
    countryInput = input("Insert a country name: ")
    countryName  = CountryInputToUpper(countryInput)

    try:

        index = CountryIndex(countryName)
        totalDeaths  = GetColumnValue(index, "total")
        maleDeaths   = GetColumnValue(index, "male")
        femaleDeaths = GetColumnValue(index, "female")
        
        print(f"{index} Total deaths:{int(totalDeaths)}  male:{maleDeaths}%  female:{femaleDeaths}%")

        PlotDeathsResults(maleDeaths, femaleDeaths, countryName, totalDeaths)

    except (IndexError, NameError, TypeError):
        print("Incorrect country name please try again.")
        commands()


#main function
def main():
    print()
    print("Covid Analyzer")
    commands()

    while(True):
        command = input("Command: ").lower()

        if(command == "ld"):
            DeathResults()

        elif(command == "cmd"):
            commands()

        elif(command == "exit"):
            break

        else:
            print("Invalid command please try again.")
            print()


if __name__ == "__main__":
    main()
