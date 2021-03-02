# import data in csv file
import logging
import os
import csv
from pprint import pprint

path = os.path.join("Resources", "budget_data.csv")

with open(path, "r") as file:
    # assumes reader API can handle files of size
    # if exceptions thrown, catch and confess
    try:
        dict_reader = csv.DictReader(file)
    except IOerror as e:
        logging.exception('')
      
    budget_dicts_list = [dict(ordered_dict) for ordered_dict in dict_reader]
    # throw error if no exception but still no data
    if not len(budget_dicts_list):
        raise ValueError('No data available')
    
# data consistency check: check for duplicates
for month_dict in budget_dicts_list:
    multi = False
    visited_num = 0
    for inner_month_dict in budget_dicts_list:
        if inner_month_dict['Date'] == month_dict['Date']:
            visited_num += 1
    if visited_num > 1:
        multi = True

        
# create new combined dict called budget_dict 
budget_dict = {}
# keeping ordered months as a separate list
ordered_months = []
for month_dict in budget_dicts_list:
    budget_dict[month_dict['Date']] = month_dict['Profit/Losses']
    ordered_months.append(month_dict['Date'])
    
    
# get total number of months
tot_months = len(budget_dict.keys())

header = "Financial Analysis"
print(header)
print("-"*(len(header)+10))
print(f"Total Months: {tot_months}")


# get net profit/loss
tot_pnl = 0
for month_key in budget_dict:
    tot_pnl += int(budget_dict[month_key])
print(f"Total: ${tot_pnl}")


# get average of the changes in "Profit/Losses" over the entire period
counter = 0
diffs_list = []
for row_dict in budget_dicts_list:
    if counter == 0:
        counter += 1
        continue
    diffs_list.append(int(row_dict['Profit/Losses']) - int(budget_dicts_list[counter - 1]['Profit/Losses']))
    counter += 1

avg_change = round((float(sum(diffs_list) / (tot_months - 1))), 2)
print(f"Average Change: ${avg_change}")


# get greatest increase in profits  
max_diff_index = diffs_list.index(max(diffs_list))
print(f"Greatest Increase in Profits: {budget_dicts_list[max_diff_index + 1]['Date']} (${diffs_list[max_diff_index]})")


# get greatest decrease in profits
min_diff_index = diffs_list.index(min(diffs_list))
# this should not go out of range since we are always skipping record 0
print(f"Greatest Decrease in Profits: {budget_dicts_list[min_diff_index + 1]['Date']} (${diffs_list[min_diff_index]})")


# export results to text file
pybank_output_path = '/home/jupyter/python-challenge/PyBank/analysis/results.txt'
with open(pybank_output_path, 'a') as file:
    # print with pretty formatting
    file.write(header)
    file.write("\n")
    file.write("-"*(len(header)+10))
    file.write("\n")
    file.write(f"Total Months: {tot_months}\n")
    file.write(f"Total: ${tot_pnl}\n")
    file.write(f"Average Change: ${avg_change}\n")
    file.write(f"Greatest Increase in Profits: {budget_dicts_list[max_diff_index + 1]['Date']} (${diffs_list[max_diff_index]})\n")
    file.write(f"Greatest Decrease in Profits: {budget_dicts_list[min_diff_index + 1]['Date']} (${diffs_list[min_diff_index]})")


        
    