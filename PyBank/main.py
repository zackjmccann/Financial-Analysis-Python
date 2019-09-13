#PyBank - Python Challenge

import os
import csv

#Path to the budget data file from PyBank directory
pybank_csv = os.path.join("../", "../", "Homework Instructions", "PyBank", "Resources", "budget_data.csv")

#Lists for the months and profit/losses
months = []
profit_losses = []

num_of_months = 0
total_pl = 0
pro_loss_total = 0

#Read into the budget data file
with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        months.append(row[0])
        profit_losses.append(int(row[1]))

    for num in profit_losses:
        total_pl += num
    
    num_of_months = str(len(months))
    pro_loss_total = str(total_pl)

    def totalMonths(allMonths):
        print("Total Months: " + allMonths)
    def sumOfProLoss(proLossSum):
        print("Profit/Loss Total: " + pro_loss_total)

#Zip the new data together
#cleaned_file = zip(months, profit_losses)

#Create a new csv document for the results
analyzed_data = os.path.join("pybank_analyzed.csv")

#Write the new file
with open(analyzed_data, 'w') as data:
    writer = csv.writer(data)
    writer.writerow([totalMonths(num_of_months)])
    writer.writerow([sumOfProLoss(pro_loss_total)])
    #writer.writerows(cleaned_file)
