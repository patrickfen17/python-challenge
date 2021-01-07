# Modules
import os
import csv

# Set path for budget file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Use total to calculate the Profit/Loss 
# Use months to count the number of months in the dataset
total = 0
months = 0
sum_change = 0
previous = 0
change_values = []

# Open the CSV
with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    # Loop through file
    for row in csvreader:

        # Total P&L and number of months
        total = total + float(row[1])
        months = months + 1
        
        # Find avg change and greatest increase and decrease 
        if months > 1:
            change = float(row[1]) - previous
            sum_change = sum_change + change
            change_values.append(change)

        # Set previous to current row P/L 
        previous = float(row[1])

average = sum(change_values) / len(change_values)

print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {months}")
print(f"Total: ${total:.0f}")
print(f"Average Change: ${average:.2f}")
print(f"Greatest Increase in Profits: (${max(change_values):.0f})")
print(f"Greatest Decrease in Profits: (${min(change_values):.0f})")

#path = os.path.join('..', 'Analysis', 'output.txt')
with open('Analysis/output.txt', 'w') as txt_file:
     txt_file.write(f"Financial Analysis \n")
     txt_file.write(f"--------------------------------- \n")
     txt_file.write(f"Total Months: {months} \n")
     txt_file.write(f"Total: ${total:.0f} \n")
     txt_file.write(f"Average Change: ${average:.2f} \n")
     txt_file.write(f"Greatest Increase in Profits: (${max(change_values):.0f}) \n")
     txt_file.write(f"Greatest Decrease in Profits: (${min(change_values):.0f})")