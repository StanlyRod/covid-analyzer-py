
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

#get current directory
currentDirectory = os.getcwd()

dfile = f"{currentDirectory}\deaths.xlsx"
vfile = f"{currentDirectory}\\full_vaccinations.xlsx"


#read excel files and catch the filenotfound error exception
def ReadExcelFile(xfile):
     try:
        readxfile = pd.read_excel(xfile)
        return readxfile

     except FileNotFoundError as fne:
        print(f"File or directory not found  {fne.filename}")
        sys.exit()


readxdfile = ReadExcelFile(dfile)
readxvfile = ReadExcelFile(vfile)


#get the country index value of the excel file
def CountryIndex(conName, excelFilePath):
    index_value = excelFilePath.index[excelFilePath['country'] == conName].tolist()[0]
    return index_value
    

#get a specific value of any column based on the country index value      
def GetColumnValue(indexValue, columnName, excelFilePath):
    value = excelFilePath.iloc[indexValue][columnName]
    return float(value)
    

#Convert the first letter of each word in the input to upper-case
def CountryInputToUpper(entryTxt):
    toAList = entryTxt.split(" ")
    wordsToUpper = list(map(lambda words: words.capitalize(), toAList))
    countrytoString = " ".join(wordsToUpper)
    return countrytoString


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

        index = CountryIndex(countryName, readxdfile)
        totalDeaths  = GetColumnValue(index, "total", readxdfile)
        maleDeaths   = GetColumnValue(index, "male", readxdfile)
        femaleDeaths = GetColumnValue(index, "female", readxdfile)
        
        print(f"{index} Total deaths:{int(totalDeaths)}  male:{maleDeaths}%  female:{femaleDeaths}%")

        PlotDeathsResults(maleDeaths, femaleDeaths, countryName, totalDeaths)

    except (IndexError, NameError, TypeError):
        print("Incorrect country name please try again.")
        commands()



def PlotVaccinationResults(maleVax, femaleVax):
    fig, ax = plt.subplots()

    gender = ["Male", "Female"]
    count  = [maleVax, femaleVax]
    
    ax.pie(count, labels=gender)
    
                 


def VaxResults():
    countryInput = input("Insert a country name: ")
    countryName  = CountryInputToUpper(countryInput)

    # try:
    index = CountryIndex(countryName, readxvfile)
    #totalVax = GetColumnValue(index, "Total", readxvfile)
    maleVax  = GetColumnValue(index, "Male", readxvfile)
    femaleVax = GetColumnValue(index, "Female", readxvfile)
    #print(f"{index} Total vaccinations {totalVax} male:{maleVax} female:{femaleVax}")

    PlotVaccinationResults(maleVax, femaleVax)
    # except:
    #     print("error")
    #     commands()

#main function
def main():
    print()
    print("Covid Analyzer")
    commands()

    while(True):
        command = input("Command: ").lower()

        if(command == "ld"):
            DeathResults()

        elif(command == "fv"):
            VaxResults()

        elif(command == "cmd"):
            commands()

        elif(command == "exit"):
            break

        else:
            print("Invalid command please try again.")
            print()


if __name__ == "__main__":
    main()
