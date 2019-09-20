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

#Functions


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

    can_one = (str(candidate[0])) + " " +(str(cand_votes[0]))
    can_two = (str(candidate[1])) + " " +(str(cand_votes[1]))
    can_three = (str(candidate[2])) + " " +(str(cand_votes[2]))
    can_four = (str(candidate[3])) + " " +(str(cand_votes[3]))

    #Calculate the Winner
    

#Create a new csv document for the results
analyzed_data = os.path.join("pypoll_analyzed.csv")

#Write the new file
with open(analyzed_data, "w", newline="") as data:
    writer = csv.writer(data, delimiter=',')
    writer.writerow(["Election Analysis"])
    writer.writerow(["Total Votes: " + num_of_votes])
    writer.writerow([can_one])
    writer.writerow([can_two])
    writer.writerow([can_three])
    writer.writerow([can_four])