Background:

Congratulations, you've made it!

It's time to put away the Excel sheet and embrace the world of programming with Python. In this assignment, you'll be using the concepts you've learned to tackle two Python challenges: PyBank and PyPoll. Both tasks present real-world situations where your newly developed Python scripting skills come in handy.

Before You Begin:

Create a new repository for this project called "python-challenge." Do not add this assignment to an existing repository.

Clone the new repository to your computer.

Inside your local Git repository, create a folder for each Python assignment and name them PyBank and PyPoll.

In each folder that you just created, add the following content:

A new file called main.py. This will be the main script to run for each analysis.

A Resources folder that contains the CSV files you used. Make sure that your script has the correct path to the CSV file.

An analysis folder that contains your text file that has the results from your analysis.

Push these changes to GitHub.

Files:

Download the necessary files to get started: [Module 3 Challenge files]

PyBank Instructions:

In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset named budget_data.csv, consisting of two columns: "Date" and "Profit/Losses."

Your task is to create a Python script that analyzes the records and calculates the following values:

The total number of months included in the dataset.
The net total amount of "Profit/Losses" over the entire period.
The changes in "Profit/Losses" over the entire period, and then the average of those changes.
The greatest increase in profits (date and amount) over the entire period.
The greatest decrease in profits (date and amount) over the entire period.
Your analysis should align with the following results:

Financial Analysis
----------------------------
Total Months: 86
Total: $22,564,198
Average Change: $-8,311.11
Greatest Increase in Profits: Aug-16 ($1,862,002)
Greatest Decrease in Profits: Feb-14 ($-1,825,558)
In addition, your final script should both print the analysis to the terminal and export a text file with the results.

PyPoll Instructions:

In this Challenge, you are tasked with helping a small rural U.S. town modernize its vote-counting process.

You will be given a set of poll data called election_data.csv, consisting of three columns: "Voter ID," "County," and "Candidate." Your task is to create a Python script that analyzes the votes and calculates the following values:

The total number of votes cast.
A complete list of candidates who received votes.
The percentage of votes each candidate won.
The total number of votes each candidate won.
The winner of the election based on popular vote.
Your analysis should align with the following results:

Election Results
-------------------------
Total Votes: 369,711
-------------------------
Charles Casper Stockham: 23.049% (85,213)
Diana DeGette: 73.812% (272,892)
Raymon Anthony Doane: 3.139% (11,606)
-------------------------
Winner: Diana DeGette
-------------------------
In addition, your final script should both print the analysis to the terminal and export a text file with the results.