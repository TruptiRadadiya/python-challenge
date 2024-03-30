# Modules
import os
import csv

# Set path to read a file
csvpath = os.path.join("Resources","budget_data.csv")

# Dictionary to store csv file data
profit_loss_dict = {"Date":[], "Profit/Losses":[]}

# Open the csv file and assign reader coontents
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row
    csv_header = next(csvreader)

    # Add data to the dictionary 
    for row in csvreader:
        profit_loss_dict["Date"].append(row[0])
        profit_loss_dict["Profit/Losses"].append(row[1])


# Calculate total number of months included in the dataset
total_months = len(profit_loss_dict["Date"])    

# Calculate net total amount of "Profit/Losses" over the entire period
total = sum(int(num) for num in profit_loss_dict["Profit/Losses"])

# Calculate changes in "Profit/Losses" over the entire period, and then the average of those changes
changes = [int(profit_loss_dict["Profit/Losses"][i]) - int(profit_loss_dict["Profit/Losses"][i-1]) for i in range(1, len(profit_loss_dict["Profit/Losses"]))]
avg_change = sum(changes) / len(changes)

# Calculate the greatest increase in profits (date and amount) over the entire period
# Initialize vatribales to keep track of greatest increase
greatest_increase = 0
greatest_increase_date = ""

# Loop through each record of profit_loss_dict
for i in range(1, len(profit_loss_dict["Profit/Losses"])):
    current_record = int(profit_loss_dict["Profit/Losses"][i])
    previous_record = int(profit_loss_dict["Profit/Losses"][i-1])
    increase = current_record - previous_record
    # Check if increase is greater than greatest increase
    if increase > greatest_increase:
        greatest_increase = increase
        greatest_increase_date = profit_loss_dict["Date"][i]

# Calculate the greatest decrease in profits (date and amount) over the entire period
# Initialize vatribales to keep track of greatest decrease
greatest_decrease = float('inf') # used positive infinity 
greatest_decrease_date = ""

# Loop through each record of profit_loss_dict
for i in range(1, len(profit_loss_dict["Profit/Losses"])):
    current_record = int(profit_loss_dict["Profit/Losses"][i])
    previous_record = int(profit_loss_dict["Profit/Losses"][i-1])
    decrease = current_record - previous_record
    # Check if decrease is lesser than greatest decrease
    if decrease < greatest_decrease:
        greatest_decrease = decrease
        greatest_decrease_date = profit_loss_dict["Date"][i]

print("Financial Analysis")
print("-----------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${avg_change:0.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Give a path of a file to write to
output_path = os.path.join("Analysis","output.txt")

# Open the file with "write" mode
with open(output_path, 'w') as textfile:

    # Write to the output.txt file
    textfile.write("Financial Analysis\n")
    textfile.write("-----------------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${total}\n")
    textfile.write(f"Average Change: ${avg_change:0.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")