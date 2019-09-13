#PyBank - Python Challenge

import os
import csv

#Path to the budget data file from PyBank directory
pybank_csv = os.path.join("../", "../", "Homework Instructions", "PyBank", "Resources", "budget_data.csv")

#Variables
months = []
profit_losses = []
total_pl = 0

#Read into the budget data file
with open(pybank_csv, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        months.append(row[0])
        profit_losses.append(int(row[1]))

    for num in profit_losses:
        total_pl += num
    
    num_of_months = (str(len(months)))
    pro_loss_total = (str(total_pl))

#Create a new csv document for the results
analyzed_data = os.path.join("pybank_analyzed.csv")

#Write the new file
with open(analyzed_data, "w", newline="") as data:
    writer = csv.writer(data, delimiter=',')
    writer.writerow(["Financial Analysis"])
    writer.writerow(["Total Months: " + num_of_months])
    writer.writerow(["Toatl Profit/Loss: " + pro_loss_total])
