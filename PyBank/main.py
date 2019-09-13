#PyBank - Python Challenge

import os
import csv

#Path to the budget data file from PyBank directory
pybank_csv = os.path.join("../", "../", "Homework Instructions", "PyBank", "Resources", "budget_data.csv")

#Lists for the months and profit/losses
months = []
profit_losses = []

#Read into the budget data file
with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        months.append(row[0])
        #profit_losses.append(row[1])

#Zip the new data together
#cleaned_file = zip(months, profit_losses)

#Create a new csv document for the results
analyzed_data = os.path.join("pybank_analyzed.csv")

#Write the new file
with open(analyzed_data, 'w') as data:
    writer = csv.writer(data)
    writer.writerow([len(months)])
    #writer.writerows(cleaned_file)
