#PyPoll - Python Challenge

import os
import csv
from collections import Counter

#Path to the election data file from PyPoll directory
pypoll_csv = os.path.join("../", "../", "Homework Instructions", "PyPoll", "Resources", "election_data.csv")

voter_id = []
county = []
voter_cand = []

candidate = []
cand_votes = []

#Read into the election data file
with open(pypoll_csv, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    
    #Place all data in list
    for row in csvreader:
            voter_id.append(row[0])
            # county.append(row[1])
            voter_cand.append(row[2])

    #Calculate the number of votes
    num_of_votes = (str(len(voter_id)))

    #List of candidates who received votes
    for x in Counter(voter_cand).keys():
        candidate.append(x)
    
    for x in Counter(voter_cand).values():
        cand_votes.append(x)


    #Calculate the percentage of total votes each candidate recevied
    total = sum(cand_votes)
    percent_one = (str(round(((cand_votes[0]/total)*100),2)))
    percent_two = (str(round(((cand_votes[1]/total)*100),2)))
    percent_three = (str(round(((cand_votes[2]/total)*100),2)))
    percent_four = (str(round(((cand_votes[3]/total)*100),2)))

    can_one = f"{str(candidate[0])}: {percent_one}% ({str(cand_votes[0])})"
    can_two = f"{str(candidate[1])}: {percent_two}% ({str(cand_votes[1])})"
    can_three = f"{str(candidate[2])}: {percent_three}% ({str(cand_votes[2])})"
    can_four = f"{str(candidate[3])}: {percent_four}% ({str(cand_votes[3])})"

    #Calculate the Winner
    winner = max(cand_votes)

#Create a new csv document for the results
analyzed_data = os.path.join("pypoll_analyzed.csv")

#Write the new file
with open(analyzed_data, "w", newline="") as data:
    writer = csv.writer(data, delimiter=',')
    writer.writerow(["Election Results"])
    writer.writerow([f"Total Votes: {num_of_votes}"])
    writer.writerow(["---------------------"])
    writer.writerow(["Candidates"])
    writer.writerow([can_one])
    writer.writerow([can_two])
    writer.writerow([can_three])
    writer.writerow([can_four])
    writer.writerow(["---------------------"])
    writer.writerow([f"Winner: {str(winner)}"])