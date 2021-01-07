# Modules
import os
import csv

# Set path for election file
csvpath = os.path.join('Resources', 'election_data.csv')

# Use total to calculate total votes 
# Use months to count the number of months in the dataset
total_votes = 0
candidate_names = {}

# Open the CSV
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Loop through file
    for row in csvreader:
        
        # Total vote counter
        total_votes = total_votes + 1
        # Add candidates to dictionary and count votes
        if row[2] in candidate_names:
            #add 1 to value 
            candidate_names[row[2]] += 1
        else:
            #add canidate to dictionary with value of 1
            candidate_names[row[2]] = 1
winner_key = max(candidate_names, key=candidate_names.get)

# Print results to terminal
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")   
print("--------------------------")
for key, value in candidate_names.items():

      print(f"{key}: = {value/total_votes:.2%} ({value})")

print("--------------------------")
print("Winner: " + (winner_key))

# Print results to text file
with open('Analysis/output.txt', 'w') as txt_file:
     txt_file.write(f"Election Results \n")
     txt_file.write(f"--------------------------------- \n")
     txt_file.write(f"Total Votes: {total_votes} \n")
     txt_file.write(f"--------------------------------- \n")
     for key, value in candidate_names.items():
        txt_file.write(f"{key}: = {value/total_votes:.2%} ({value}) \n")
     txt_file.write(f"--------------------------------- \n")
     txt_file.write(f"Winner: " + (winner_key))