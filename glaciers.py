import csv

from typing import Collection

import matplotlib as plt

from pathlib import Path

class Glacier:

    def __init__(self, glacier_id, name, unit, lat, lon, code):

        self.glacier_id = glacier_id

        self.name = name

        self.unit = unit


        # Location

        self.lat = lat

        self.lon = lon

        self.code = code

    def add_mass_balance_measurement(self, year, mass_balance, boolean_value):
        # a boolean value indicating whether this is a partial (sub-region) measurement or not
        
        raise NotImplementedError


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

        self.my_glacier = []

        for row in csv_reader:
            # row = [glacier_id, name, unit, lat, lon, code]
            glacier_id = row[2]
            name = row[1]
            unit = row[0]
            lat = float(row[5])
            lon = float(row[6])
            code = int(row[7]+row[8]+row[9])

            # Store the data in my_glacier
            self.my_glacier.append(Glacier(glacier_id, name, unit, lat, lon, code))

        file.close()
    
    def read_mass_balance_data(self, file_path):
        
        raise NotImplementedError

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

# To test the output 
for item in collection.my_glacier:
    print(item.name)
    
print(collection.my_glacier[100].code)