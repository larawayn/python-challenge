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
    
    candidate_info = {}

    # Read each row of data after the header
    for row in csvreader: 
        candidate = str(row[0])
    #create dictionary
        if row in candidate:
            candidate_info(str(row[0])) += 1
        else:
            csvreader[row] = 1 
        
    for key, value in candidate.items(): 
        print ("% d : % d"%(key, value))


    
    print("Total Votes:   ", total_votes)
    print("-------------------")