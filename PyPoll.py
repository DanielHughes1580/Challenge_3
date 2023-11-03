# Initializing environments
import os
import csv

# Defining Variables
total = 0
ccs = "Charles Casper Stockham"
ccstot = 0
ddg = "Diana DeGette"
ddgtot = 0
rad = "Raymon Anthony Doane"
radtot = 0

# Creating Pathway
csvpath = os.path.join('..', 'Resources','election_data.csv')

#  Main Code
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        #Total of Votes
        total = total + 1
        # Counting Votes for Specific Candidates
        if row[2] == ccs:
            ccstot = ccstot + 1
        if row[2] == ddg:
            ddgtot = ddgtot + 1
        if row[2] == rad:
            radtot = radtot + 1
        # Candidate Percentages
        ccsper = (ccstot/total)*100
        ddgper = (ddgtot/total)*100
        radper = (radtot/total)*100
        winner = max(ccstot,ddgtot,radtot)
        # Calculate Winner
        if winner == ccstot:
            winner_name = ccs
        if winner == ddgtot:
            winner_name = ddg
        if winner == radtot:
            winner_name =  rad
        
# printing the results   
print("Election Results") 
print("---------------------------------")       
print(f"The Total Amount of Votes is: {total}")
print("---------------------------------")
print(f"Charles Casper Stockham: {round(ccsper,3)}% ({ccstot})")
print(f"DianneDeGette: {round(ddgper,3)}% ({ddgtot})")
print(f"Raymon Anthony Doane: {round(radper,3)}% ({radtot})")
print("---------------------------------")
print(f"The Winner is: {winner_name}")

# Exporting Results to Text File
txt = open("PyPoll.txt", "w")
lines = ["Election Results", 
         "---------------------------------", 
         f"The Total Amount of Votes is: {total}",  
         "---------------------------------",
         f"Charles Casper Stockham: {round(ccsper,3)}% ({ccstot})",
         f"DianneDeGette: {round(ddgper,3)}% ({ddgtot})", 
         f"Raymon Anthony Doane: {round(radper,3)}% ({radtot})", 
         "---------------------------------", 
         f"The Winner is: {winner_name}"
           ]
for line in lines:
    txt.write(line)
    txt.write('\n')
