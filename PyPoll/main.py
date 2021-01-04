# First we'll import the os module
# This will allow us to create file paths across operating systems
import os 

# Module for reading CSV files
import csv


import sys

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

# Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    print("Election Results")
    print("-------------------")
    #assign variables
    total_votes = 0
    vote_count = {'Khan' : 0, 'Correy' : 0, 'Li': 0, "O'Tooley": 0}
    
    # Read each row of data after the header
    for row in csvreader: 
        name = row[2]
        total_votes = total_votes + 1
    #create dictionary
        if name not in vote_count:
            vote_count[name] = 0
        else:
            vote_count[name] += 1 
            
    winner = max(vote_count, key=vote_count.get)
    
    #Possible output of combined dictionary -- NOT WORKING
    #combined_dictionary = {k: [vote_count[k], voter_percentage.get(k)] for k in vote_count}
    #combined_dictionary.update({k: [None, voter_percentage[k]] for k in voter_percentage if k not in vote_count})
    #print("Khan:  ", f'{combined_dictionary["Khan"]}')
    #print("O'Tooley:  ", f'{combined_dictionary["O'Tooley"]}')
    
    print("Total Votes:   ", total_votes)
    print("-------------------")
    for key, votes in vote_count.items():
            voter_percentage = round((votes/ total_votes)* 100, 3)
            print(f'{key}: {voter_percentage}%  ({votes})')
    #print("Khan:  ", f'{voter_percentage["Khan"]}', "("+f'{vote_count["Khan"]}'+")")
    #print("Correy:  ", f'{voter_percentage["Correy"]}', "("+f'{vote_count["Correy"]}'+")")
    #print("Li:  ", f'{voter_percentage["Li"]}', "("+f'{vote_count["Li"]}'+")")
   # print(f'"O'Tooley:  " , {voter_percentage["O'Tooley"]}', "("+f'{vote_count["O'Tooley"]}'+")")
   
    print("-------------------")
    print("Winner:  ", winner)
    print("-------------------")

        # Specify the file to write to
output_path = os.path.join("Analysis", "Python-Challenge.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as datafile:   
     # Initialize writer
     print("\n-------", file=datafile)
     # write rows
     #writer.writerow(["Election Results"])
     #writer.writerow(["Total Votes:   ", total_votes])
     #writer.writerow(["-------------------"])
     #writer.writerow([""])
     for key, votes in vote_count.items():
            voter_percentage = round((votes/ total_votes)* 100, 3)
            print(f'{key}: {voter_percentage}%  ({votes})', file=datafile)


     #writer.writerow(["O'Tooley:  ", f'{voter_percentage["O'Tooley"]}', "("+f'{vote_count["O'Tooley"]}'+")"])
     #writer.writerow(["-------------------"])
     #writer.writerow(["Winner:  ", winner])
     #writer.writerow(["-------------------"])

