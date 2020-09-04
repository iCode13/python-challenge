#!/opt/conda/bin/python

# import data in csv file
import logging 
import os
import csv
from pprint import pprint

path = os.path.join("Resources", "election_data.csv")

with open(path, "r") as file:
    # assumes reader API can handle files of size
    # if exceptions thrown, catch and confess
    try:
        dict_reader = csv.DictReader(file)
    except IOerror as e:
        logging.exception('')
        
    election_dicts_list = [dict(ordered_dict) for ordered_dict in dict_reader]
    # throw error if no exception but still no data
    if not len(election_dicts_list):
        raise ValueError('No data available')
        
    
# get total number of votes
tot_votes = len(election_dicts_list)

header = "Election Results"
print(header)
print("-"*(len(header)+10))
print(f"Total Votes: {tot_votes}")
print("-"*(len(header)+10))


# get list of candidates, their votes and percentages
candidates_dict = {}

for row_dict in election_dicts_list:
    # for name duplicates, only first value is captured   
    if row_dict['Candidate'] not in candidates_dict:
        candidates_dict[row_dict['Candidate']] = 1
    else:
        candidates_dict[row_dict['Candidate']] += 1

for candidate_name in candidates_dict.keys():
        print(f"{candidate_name}: {candidates_dict[candidate_name]/tot_votes*100:.3f}% ({candidates_dict[candidate_name]})")
        
        
# find the winner of the election
winner = None
winning_total = 0
for candidate_name in candidates_dict.keys():
    if candidates_dict[candidate_name] > winning_total:
        winner = candidate_name
        winning_total = candidates_dict[candidate_name]
print("-"*(len(header)+10))
print(f"Winner: {winner}")
print("-"*(len(header)+10))
  
    
# export results to text file
pypoll_output_path = '/home/jupyter/python-challenge/PyPoll/analysis/results.txt'

with open(pypoll_output_path, 'a') as file:
    # print with pretty formatting
    file.write(header)
    file.write("\n")
    file.write("-"*(len(header)+10)) 
    file.write("\n")
    file.write(f"Total Votes: {tot_votes}\n")
    file.write("-"*(len(header)+10)) 
    file.write("\n")
    for candidate_name in candidates_dict.keys():
        file.write(f"{candidate_name}: {candidates_dict[candidate_name]/tot_votes*100:.3f}% ({candidates_dict[candidate_name]})\n")
    file.write("-"*(len(header)+10))
    file.write("\n")
    file.write(f"Winner: {winner}\n")
    file.write("-"*(len(header)+10))
