import csv
from pathlib import Path
import re


class TableDataProcessing:
    def __init__(self, path = Path.home() / 'Desktop'):
        self.path = path

    # parses data from .wth file and returning list of lines with the list of words inside
    def wthTableParse(self, file_name):
        self.wth_file_name = file_name + ".WTH"
        self.pathToFile = self.path / self.wth_file_name  # creating path to file.wth

        # Creating the list of lines and list of words inside the list of lines
        self.dataList = []
        with open(self.pathToFile, "rt") as wthFile:
            for line in wthFile:
                self.dataList.append(re.split(' +', line))



        del self.wth_file_name
        return self.dataList



    # parses data from .csv file and returning list of lines with the list of words inside
    def csvTableParse(self, file_name):
        self.csv_file_name = file_name + ".csv"

        self.pathToFile = self.path / self.csv_file_name # creating path to file.csv

        self.dataList = []
        with open(self.pathToFile, "rt") as csvFile:
            self.csvObject = csv.reader(csvFile)
            for row in self.csvObject:
                self.dataList.append(row)

            del self.csvObject
            del self.csv_file_name

        return self.dataList




