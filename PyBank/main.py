#PyBank - Python Challenge

import os
import csv

#Path to the budget data file from PyBank directory
pybank_csv = os.path.join("../", "../", "Homework Instructions", "PyBank", "Resources", "budget_data.csv")

#Variables
months = []
profit_loss = []
change_list = []
total_pl = 0
sum_change = 0

#Functions
def average_change(pro_loss):
    current_month = 1
    prev_month = 0
    for x in pro_loss:
        if current_month <= 85:
            x = pro_loss[current_month] - pro_loss[prev_month]
            change_list.append(x)
            current_month += 1
            prev_month += 1

def increase(changes):
    greatest_increase = 0
    value = 0
    for x in changes:
        while value <= 84:
            if changes[value] > greatest_increase:
                greatest_increase = changes[value]
            value += 1
    return greatest_increase

def decrease(changes):
    greatest_decrease = 0
    value = 0
    for x in changes:
        while value <= 84:
            if changes[value] < greatest_decrease:
                greatest_decrease = changes[value]
            value += 1
    return greatest_decrease


#Read into the budget data file
with open(pybank_csv, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)

    #Make a list of all the Months and the profit/losses
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))
    
    #Find the total profit/loss
    for num in profit_loss:
        total_pl += num

    #Calculate the number of months
    num_of_months = (str(len(months)))

    #Calculate the total profit loss
    pro_loss_total = (str(total_pl))

    #Calculate the average change
    average_change(profit_loss)
    
    for change in change_list:
        sum_change += change

    avg_change = (str(round((sum_change/85),2)))
    grt_increase = (str(increase(change_list)))
    grt_decrease = (str(decrease(change_list)))

#Create a new csv document for the results
analyzed_data = os.path.join("pybank_analyzed.csv")

#Write the new file
with open(analyzed_data, "w", newline="") as data:
    writer = csv.writer(data, delimiter=',')
    writer.writerow(["Financial Analysis"])
    writer.writerow(["Total Months: " + num_of_months])
    writer.writerow(["Total Profit/Loss: $" + pro_loss_total])
    writer.writerow(["Average Profit/Loss Change: $" + avg_change])
    writer.writerow(["Greatest Increase in Profits: $" + grt_increase])
    writer.writerow(["Greatest Decrease in Profits: $" + grt_decrease])
