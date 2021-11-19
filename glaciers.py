import csv

from typing import Collection

import matplotlib as plt

from pathlib import Path

class Glacier:

    def __init__(self, glacier_id, name, unit, lat, lon, code):

        self.glacier_id = glacier_id

        self.name = name

        self.unit = unit

        self.lat = lat

        self.lon = lon

        self.code = code

        # To store the year, mass_balance in dictionary
        self.mass_balance_measurement = {}

    def add_mass_balance_measurement(self, year, mass_balance, partial_state):

        # Check if is partial and check the year in each glacier id whether if it is partial
        if partial_state == False & mass_balance_measurement[year]['partial_state'] == 
            mass_balance_measurement[year]["mass_balance"] += mass_balance
        if partial_state == True 
            mass_balance_measurement[year]["mass_balance"] = mass_balance

        # Store the new mass balance, and the , with the coresponding new year
        self.mass_balance_measurement[year] = {'mass_balance','partial_state'} 


    def plot_mass_balance(self, output_path):

        raise NotImplementedError



class GlacierCollection:


    def __init__(self, file_path):
        
        # Read the dataset of the glacier_id, name, unit, lat, lon, code
        file = open(file_path)
        csv_reader = csv.reader(file)

        # the first line is the header
        header = []
        header = next(csv_reader) 

        self.glacier_dataset = {}

        for row in csv_reader:
            # row = [glacier_id, name, unit, lat, lon, code]
            glacier_id = row[2]
            name = row[1]
            unit = row[0]
            lat = float(row[5])
            lon = float(row[6])
            code = int(row[7]+row[8]+row[9])

            # Store the data in my_glacier
            my_glacier = Glacier(glacier_id, name, unit, lat, lon, code)
            self.glacier_dataset[glacier_id] = my_glacier

        file.close()
    
    def read_mass_balance_data(self, file_path):

        # Read the dataset of the year and mass_balance
        file = open(file_path)
        csv_reader = csv.reader(file)

        # the first line is the header
        header = []
        header = next(csv_reader) 

        for row in csv_reader:
            # row = [glacier_id, year,Lower Bound, Upper Bound, mass_balance]
            glacier_id_EE = row[2]
            year = row[3]
            Lower_Bound = int(row[4])
            Upper_Bound = int(row[5])

            mass_balance = float(row[11])
            
            # Check if it is partial measurement
            if Lower_Bound == 9999 & Upper_Bound == 9999:
                partial_state = False 
            else:
                partial_state = True

            # Match the id with corresponding mass_balance_measurement
            self.glacier_dataset[glacier_id_EE].add_mass_balance_measurement(year,mass_balance,partial_state)

        file.close()

    def find_nearest(self, lat, lon, n):

        """Get the n glaciers closest to the given coordinates."""

        raise NotImplementedError
    

    def filter_by_code(self, code_pattern):

        """Return the names of glaciers whose codes match the given pattern."""

        raise NotImplementedError


    def sort_by_latest_mass_balance(self, n, reverse):

        """Return the N glaciers with the highest area accumulated in the last measurement."""

        raise NotImplementedError


    def summary(self):

        raise NotImplementedError


    def plot_extremes(self, output_path):

        raise NotImplementedError


# Import the csv file, sheet A
file_path_A = Path("./sheet-A.csv")
collection = GlacierCollection(file_path_A)

# To test the output A
for item in collection.glacier_dataset:
    print(item.name)
    
print(collection.glacier_dataset[100].code)

# Import the csv file, sheet EE
file_path_EE = Path("./sheet-EE.csv")

collection.read_mass_balance_data(file_path_EE)
# To test the output EE
# print(collection.glacier_dataset[4].mass_balance_measurement)
