# import modules
import os 
import csv
import sys

#Create path for CSV
csvpath = os.path.join('Resources', 'budget_data.csv')

#Open CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # Read the header row first 
    csv_header = next(csvreader)
    
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
    print("Financial Analysis")
    print("-------------------")
    print("Total Months:  ", total_months)
    print("Total:  ", '$' + format(net_total_amount,'.2f'))
    print("Average Change:  ", '$' +  str(format(average_change,'.2f')))
    print("Greatest Increase in Profits:   ", greatest_increase_month, '($' + format(greatest_increase,'.2f') + ')')
    print("Greatest Decrease in Profits:   ", greatest_decrease_month, '($' + format(greatest_decrease,'.2f') + ')')   
    
#Specify the text file to print to
output_path = os.path.join("Analysis", "Python-Challenge.txt")

# Open the txt file
with open(output_path, 'w', newline='') as datafile:   
    # print rows to txt file
    print("Financial Analysis", file=datafile)
    print("-------------------", file=datafile)
    print("Total Months:  ", total_months, file=datafile)
    print("Total:  ", '$' + format(net_total_amount,'.2f'), file=datafile)
    print("Average Change:  ", '$' +  str(format(average_change,'.2f')), file=datafile)
    print("Greatest Increase in Profits:   ", greatest_increase_month, '($' + format(greatest_increase,'.2f') + ')', file=datafile)
    print("Greatest Decrease in Profits:   ", greatest_decrease_month, '($' + format(greatest_decrease,'.2f') + ')', file=datafile)   
 # Close file
datafile.close()   
     