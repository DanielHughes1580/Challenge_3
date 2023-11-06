# Initializing environments
import os
import csv

# Defining Variables
budgetlist = []
monthlist = []
total = 0
money = 0
prevrow = 0

# Creating Pathway
csvpath = os.path.join('budget_data.csv')

# Main Code
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        #Find Totals
        total = total + 1
        month = row[0]
        money = money + int(row[1])
        #Creating Lists to Store Seperated Data
        budgetlist.append(int(row[1]) - int(prevrow))
        monthlist.append(row[0])
        prevrow = int(row[1])
        #Average of the changes in Profits/Losses
        combine = sum(budgetlist) - budgetlist[0]
        avg = round(combine/85,2)
        #Minimum and Maximums
        maximum = max(budgetlist)
        minimum = min(budgetlist)
        maxindex = budgetlist.index(maximum)
        minindex = budgetlist.index(minimum)
        maxname = monthlist[maxindex]
        minname = monthlist[minindex]

# Printing the Results
print("Financial Analysis")
print("---------------------------------") 
print(f"Total month: {total}")
print(f"Total: ${money}")
print(f"The Average Change is: ${avg}"),
print(f"Greatest Increase in Profits: {maxname} (${maximum})"),
print(f"Greatest Decrease in Profits: {minname} (${minimum})")

# Exporting Results to Text File
txt = open("PyBank.txt", "w")
lines = ["Financial Analysis",
         "---------------------------------",
         f"Total month: {total}",
         f"Total: ${money}", 
         f"The Average Change is: ${avg}",
         f"Greatest Increase in Profits: {maxname} (${maximum})",
         f"Greatest Decrease in Profits: {minname} (${minimum})"]
for line in lines:
    txt.write(line)
    txt.write('\n')
