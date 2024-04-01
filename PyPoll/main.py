# Modules
import os
import csv

# Set path to read a 'election_data.csv' file
csvpath = os.path.join("Resources","election_data.csv")

# Dictionary to store csv file data
election_dict = {"Ballot_id":[], "County":[], "Candidate":[]}

# Open the csv file and assign reader coontents
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    # Read the header row
    csv_header = next(csvreader)

    # Add data to the election_dict dictionary
    for row in csvreader:
        election_dict["Ballot_id"].append(row[0])
        election_dict["County"].append(row[1])
        election_dict["Candidate"].append(row[2])

# Calculate the total number of votes cast
total_votes = len(election_dict["Ballot_id"])

# A complete list of candidates who received votes
# Initialize a candidates_votes_dict dictionary to hold candidates and associated votes from the election_dict
candidates_votes_dict = {}

# Loop through candidates list from election_dict
for candidate in election_dict["Candidate"]:

    # Count occurances of each candidate to calculate total vote for each candidate
    if candidate in candidates_votes_dict:
        candidates_votes_dict[candidate] += 1
    else:
        candidates_votes_dict[candidate] = 1

    # Check if the candidate is already added to the candidates_list
    if candidate not in candidates_votes_dict:
        # Add the unique candidate to the candidates_list
        candidates_votes_dict.append(candidate)

# print the total number of votes each candidate won and the percentage of votes each candidate won
def print_candidate_result(dict):
    for candidate, votes in dict.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:0.3f}% ({votes})")

# Calculate the winner of the election based on popular vote
# Find the maximum votes from candidates_votes_dict using max function
max_votes = max(candidates_votes_dict.values())

# Set the candidate as a winner from the list of candidates who has maximum votes as calculated max_votes
winner = [candidate for candidate, votes in candidates_votes_dict.items() if votes == max_votes]

# Print the results to the terminal
print("Election Results")
print("--------------------------------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------------------------------")
print_candidate_result(candidates_votes_dict)
print("--------------------------------------------------")
print(f"Winner: {', '.join(winner)}") # if more than one winners join them by ',' else print the one winner 
print("--------------------------------------------------")

# Give a path of a file to write to
output_path = os.path.join("Analysis","output.txt")

# Open the file with "write" mode
with open(output_path, 'w') as textfile:

    # Write to the output.txt file
    textfile.write("Election Results\n")
    textfile.write("-----------------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("-----------------------------------\n")
    for candidate, votes in candidates_votes_dict.items():
        percentage = (votes / total_votes) * 100
        textfile.write(f"{candidate}: {percentage:0.3f}% ({votes})\n")
    textfile.write("-----------------------------------\n")
    textfile.write(f"Winner: {', '.join(winner)}\n")
    textfile.write("-----------------------------------\n")