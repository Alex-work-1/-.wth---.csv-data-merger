from TableDataProcessing import TableDataProcessing
from HEV import HEV


import random

from pathlib import Path

import os

import csv

from datetime import datetime


default_path = Path.home() / 'Desktop' / 'weatherdata'
current_path = default_path

current_path_processed = current_path / 'Weather_data_Processed'


def instructions():
    print("*** Instructions: By default the program works with folder named \"weatherdata\" on Desktop. You can change the working directory in the settings. ***", end = "\n\n")

def intro():
    print("Starting E.D.S. system v1...", end = "\n\n")
    HEV.say('Voice system is enabled.')
    HEV.say('Welcome to the E.D.S. version 1, data merging system.')
    HEV.say('This system was designed to work with NASA weather data files.')
    HEV.say('How can I help you?')

def exit_voice():
    if random.randint(0, 1) == 0:
        HEV.say('NOOOOOOOOOOOOOOO!!!!')
    else:
        HEV.say('Thank you for using the E.D.S. system.')



def settings():
    global default_path
    global current_path

    settings_choice = input(f'''Would you like to change the current path: "{current_path}" or restore default path?
1) Yes, change the current path (example: {Path.home() / "weatherdata"})
2) No, return to main menu
3) Restore default settings
''')
    if settings_choice == '1':
        current_path = input('Enter the new path')
        print(f"The current path is changed to {current_path}")
    elif settings_choice == '2':
        pass
    elif settings_choice == '3':
        current_path = default_path
        print("Restored to default path.")
    else:
        print("Error: Wrong input.")






def specificFileMerge(name):

    # wth data preparation
    wthData = merger.wthTableParse(name)
    wthData = wthData[4:] # removes first 4 lines with names 




    Path.mkdir(current_path_processed, exist_ok = True)
    new_csv_file = str(current_path_processed / name) +".csv"


    with open(new_csv_file, "wt") as csvFile:
        writer = csv.writer(csvFile)


        # wthData filling
        writer.writerow(["tmin", "tmax", 'rain', 'solar', 'year', 'day of the year'])
        year = 19
        for info in wthData:
            if info[0][0:2] == '00':
                year = 20
            writer.writerow([info[3], info[2], info[4], info[1], f"{year}{info[0][0:2]}", info[0][2:]])

    # csvData filling

    #find index of last date of wthData in csvData

    last_wth_year = "20" + wthData[-1][0][:2] # last year

    last_wth_day = wthData[-1][0][2:] # last day

    last_wth_date = datetime.strptime(f"{last_wth_year} {last_wth_day}", '%Y %j').date()

    csvData = merger.csvTableParse(name)

    start_csv_index = [i[6] for i in csvData].index(str(last_wth_date)) + 1
    csvData = csvData[start_csv_index:]

    with open(new_csv_file, "at") as csvFile:
        writer = csv.writer(csvFile)
        for info in csvData:
            writer.writerow([info[8], info[7], info[10], info[9], info[2], info[5]])


    print(new_csv_file)
    
def merge_all_files():
    try:
        files = [File for File in os.listdir(current_path) if os.path.isfile(current_path / File)] # getting file list without dirrectories

        files_without_extention = {File.split('.')[0] for File in files} #removing extenstions and file dublicating
        try:
            files_without_extention.remove("") # removing empty elements produced by system files
        except:
            pass

        del files


        for fileName in files_without_extention:
            try:
                specificFileMerge(fileName)
            except:
                print(f"Error 2: The file wiht the name \"{fileName}\" doesn't have doesn't have extentions \".csv\" or \".wth\".")

    except:
        print(f"Error 2.1: It seems there is no such dirrectory {current_path}")



def choose_action():
        while True:
            print("What would you like to do?")
            chouse = input("""
Enter 1 of numbers below to select action.
1) Merge a specific files
2) Merge all files in the folder
3) Settings
0) Exit
""")
            if chouse == '0':
                print("Closing program...")
                merger.clearCashe()
                break

            elif chouse == '1':
                fileName = input("Enter the name of the file (without extension): \n")
                try:
                    specificFileMerge(fileName)
                except:
                    print(f"Error 1: The files with the name \"{fileName}\" and extensoins \".wth\" or \".csv\" are not found.")
                    continue
            elif chouse == '2':
                print("Merging all files from folder")

                merge_all_files()

            elif chouse == '3':
                try:
                    settings()
                except:
                    print("Error 3: The wrong user input (input must be a number).")

                continue
            else:
                print("Error")



if __name__ == "__main__":
    # setUp libraries
    merger = TableDataProcessing(path = default_path)
    HEV = HEV()

    # Instructions to computer
    instructions()
    intro()

    choose_action()
    exit_voice()
