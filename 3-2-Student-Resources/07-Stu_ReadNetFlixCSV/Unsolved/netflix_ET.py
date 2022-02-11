# Modules
import os
import csv

# Prompt user for video lookup
video = input("What show or movie are you looking for? ")

# Set path for file
csvpath = os.path.join('..', 'Resources', 'netflix_ratings.csv')

# Open the CSV
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')

    # Loop through looking for the video
    csv_header = next (csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
                
    

