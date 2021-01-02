# First we'll import the os module
# This will allow us to create file paths across operating systems
import os 

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

# Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    print("Financial Analysis")
    print("-------------------")
# Assign variables  
    total_months = 0
    net_total_amount = 0
    monthly_profit = 0
    profit_losses = []
    greatest_increase = 0
    greatest_decrease = 0
    # Read each row of data after the header
    for row in csvreader: 
    #find total_net amount
        net_total_amount = int(net_total_amount) + int(row[1])
    #find total months
        total_months = total_months + 1
    #find average_change
        change =  int(row[1]) - int(monthly_profit)
        profit_losses.append(change)
        monthly_profit = int(row[1])
    #find greatest increase month
        if change >= greatest_increase:
            greatest_increase = change
            greatest_increase_month = row[0]
    #find greatest decrease month
        if change <= greatest_decrease:
            greatest_decrease = change
            greatest_decrease_month = row[0]
    #remove first item in profit_losses
    profit_losses.pop(0)
    #find average change
    average_change = (sum(profit_losses)/len(profit_losses,))
    
    #format and print Analysis
    print("Total Months:  ", total_months)
    print("Total:  ", '$' + format(net_total_amount,'.2f'))
    print("Average Change:  ", '$' +  str(format(average_change,'.2f')))
    print("Greatest Increase in Profits:   ", greatest_increase_month, '($' + format(greatest_increase,'.2f') + ')')
    print("Greatest Decrease in Profits:   ", greatest_decrease_month, '($' + format(greatest_decrease,'.2f') + ')')   
    
    # Specify the file to write to
output_path = os.path.join("Analysis", "Python-Challenge.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as datafile:   
     # Initialize writer
     writer = csv.writer(datafile, delimiter=' ')
     # write rows
     writer.writerow(["Financial Analysis"])
     writer.writerow(["-------------------"])
     writer.writerow(["Total Months:  ", total_months])
     writer.writerow(["Total:  ", '$' + format(net_total_amount,'.2f')])
     writer.writerow(["Average Change:  ", '$' +  str(format(average_change,'.2f'))])
     writer.writerow(["Greatest Increase in Profits:   ", greatest_increase_month, '($' + format(greatest_increase,'.2f') + ')'])
     writer.writerow(["Greatest Decrease in Profits:   ", greatest_decrease_month, '($' + format(greatest_decrease,'.2f') + ')'])
     

    