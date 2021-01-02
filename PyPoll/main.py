# First we'll import the os module
# This will allow us to create file paths across operating systems
import os 

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)

# Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    print("Election Results")
    print("-------------------")
    #assign variables
    total_votes = 0
    candidate_list = []

    # Read each row of data after the header
    for row in csvreader: 
    #find total_votes
        total_votes = total_votes + 1
        


    
    print("Total Votes:   ", total_votes)
    print("-------------------")