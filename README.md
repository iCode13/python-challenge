# Python Challenge - Py Me Up, Charlie

In this assignment, Python scripting and concepts are used to complete the two Python Challenges, PyBank and PyPoll. 
    
## Objectives & Solution Approach (refer to text files for Python scripts)

### PyBank

Objective is to create a script for analyzing the financial records of a company. A set of financial data called budget_data.csv is provided for analysis, with the dataset consisting of two columns: date and profits/losses.
   
Beginning with the import of some useful libraries and setting up a path to the data file (in csv format), the file is read, an exception check is performed, and an ordered list of the data is created. The data is then checked for duplicates. Next, a dictionary is created with the months ordered.

The list or dictionary are used to perform the following calculations:

* The total number of months included in the dataset.
The 'len' function is applied to the list of dictionary keys to calculate the total number of months.

* The net total amount of "Profit/Losses" over the entire period.
A counter is created to traverse the dictionary and add up the values for all the keys.
    
* The average of the changes in "Profit/Losses" over the entire period.
A change in profit/loss is calculated for each month as compared to the previous month, and added to the list using 'append' function. This does not apply to the first month on the list, since no comparison can be made. The average of the changes is then calculated, after leaving out the first month.

* The greatest increase in profits (date and amount) over the entire period.
The 'max' function is used to calculate this.
  
* The greatest decrease in profits (date and amount) over the entire period.
The 'min' function is used to calculate this.
    
The f-string method is used to print results of the analysis. The 'with' statement is used in conjunction with 'file.write' method to export analysis results as a text file.

### PyPoll

Objective is to help a small, rural town modernize its vote-counting process, create a python script to analyze the votes for each candidate and write out the analysis as a text file. A set of poll data is provided called election_data.csv, with the dataset composed of three columns: voter id, county, and candidate.

Beginning with the import of some useful libraries and setting up a path to the data file (in csv format), the file is read, an exception check is performed, and an ordered list of the data is created. This list is then used to perform the following calculations:

* The total number of votes cast.
The 'len' function is applied to the list to calculate the total number of votes cast.

* A complete list of candidates who received votes, the percentage of votes each candidate won, the total number of votes each candidate won.
The list is traversed, and a new dictionary is created with all unique candidate names, their respective total votes and percentages.

* The winner of the election based on popular vote.
A counter is created to traverse the dictionary and find the candidate with the highest number of votes.
  
The f-string method is used to print results of the analysis. The 'with' statement is used in conjunction with 'file.write' method to export analysis results as a text file. Computation takes some time due to the larger than usual size of the dataset.

## Technologies Used
    * Python 3.7