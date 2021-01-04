# import modules
import os 
import csv
import sys

#Create path for CSV
csvpath = os.path.join('Resources', 'election_data.csv')

#Open CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # Read the header row first 
    csv_header = next(csvreader)
    
    
    #assign variables
    total_votes = 0
    vote_count = {'Khan' : 0, 'Correy' : 0, 'Li': 0, "O'Tooley": 0}
    
    # Read each row of data after the header
    for row in csvreader: 
        #Assign candidate name from CSV column
        name = row[2]
        #Calculate total votes
        total_votes = total_votes + 1
        #Add votes to dictionary for corresponding name
        if name not in vote_count:
            vote_count[name] = 0
        else:
            vote_count[name] += 1 
    #Find winner
    winner = max(vote_count, key=vote_count.get)
    
    #print output
    print("Election Results")
    print("-------------------")
    print("Total Votes:   ", total_votes)
    print("-------------------")
    for key, votes in vote_count.items():
        voter_percentage = format((votes/ total_votes * 100), '.3f')
        print(f'{key}: {voter_percentage}%  ({votes})')
    print("-------------------")
    print("Winner:  ", winner)
    print("-------------------")

# Specify the text file to print to
output_path = os.path.join("Analysis", "Python-Challenge.txt")

# Open the txt file
with open(output_path, 'w', newline='') as datafile:   
    # print rows to txt file
    print("Election Results", file=datafile)
    print("-------------------", file=datafile)
    print("Total Votes:   ", total_votes, file=datafile)
    print("-------------------", file=datafile)
    for key, votes in vote_count.items():
        voter_percentage = format((votes/ total_votes * 100), '.3f')
        print(f'{key}: {voter_percentage}%  ({votes})', file=datafile)
    print("-------------------", file=datafile)
    print("Winner:  ", winner, file=datafile)
    print("-------------------", file=datafile)
# Close file
datafile.close()

