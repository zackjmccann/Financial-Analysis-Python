#PyPoll - Python Challenge

import os
import csv

#Path to the election data file from PyPoll directory
pypoll_csv = os.path.join("../", "../", "Homework Instructions", "PyPoll", "Resources", "election_data.csv")

voter_id = []
county = []
candidate = []

#Functions
def list_all_candidates(all_candidates):
    candidate_list = []
    for x in all_candidates: 
        if x not in candidate_list: 
            all_candidates.append(x)
    return candidate_list

#Read into the election data file
with open(pypoll_csv, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    
    #Place all data in list
    for row in csvreader:
            voter_id.append(row[0])
            county.append(row[1])
            candidate.append(row[2])

    #Calculate the number of votes
    num_of_votes = (str(len(voter_id)))

    #List of candidates who received votes
    all_cans = list_all_candidates(candidate)

#Create a new csv document for the results
analyzed_data = os.path.join("pypoll_analyzed.csv")

#Write the new file
with open(analyzed_data, "w", newline="") as data:
    writer = csv.writer(data, delimiter=',')
    writer.writerow(["Election Analysis"])
    writer.writerow(["Total Votes: " + num_of_votes])
    writer.writerow(["Test Row: " + all_cans])