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
with open(pybank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        months.append(row[0])
        profit_losses.append(int(row[1]))

    for num in profit_losses:
        total_pl += num
    
    num_of_months = (str(len(months)))
    pro_loss_total = (str(total_pl))

#Zip the new data together
# cleaned_file = zip(num_of_months, pro_loss_total)
cleaned_file = zip([num_of_months], [pro_loss_total])

#Create a new csv document for the results
analyzed_data = os.path.join("pybank_analyzed.csv")

#Write the new file
with open(analyzed_data, 'w') as data:
    writer = csv.writer(data)
    # writer.writerow(["months",'pro_loss_total'])
    # writer.writerow([pro_loss_total])
    writer.writerows(cleaned_file)
