import os
import csv
from pathlib import Path

file = Path("python_challenge", "pybank", "resources", "budget_data.csv")

total_months = []
total_profit = []
monthly_change = []

with open(file) as budget:
    csvreader = csv.reader(budget, delimiter=",")

    header = next(csvreader)

    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    for i in range(len(total_profit)-1):

        monthly_change.append(total_profit[i+1]-total_profit[i])

    max_increase = max(monthly_change)
    max_decrease = min(monthly_change)

    print("Financial Analysis")
    print ("----------------------------")
    print (f"Total Months{len(total_months)}")
    print (f"Total: ${sum(total_profit)}")
    print (f"Average Change: ${round(sum(monthly_change)/ len(monthly_change),2)}")
    print (f"Greatest Increase in Profits: {total_months[max_increase]}(${(str(max_increase))})")
    print (f"Greatest Decrease in Profits: {total_months[max_decrease]}(${(str(max_decrease))})")

    output = Path("python-challenge", "pybank", "analysis",+ "Financial_Analysis_Summary.txt")

    with open(output, "w") as file:

        file.write("Financial Analysis")
        file.write("\n")
        file.write("----------------------------")
        file.write("\n")
        file.write(f"Total Months: {len(total_months)}")
        file.write("\n")
        file.write(f"Total: ${sum(total_profit)}")
        file.write("\n")
        file.write(f"Average Change: {round(sum(monthly_change)/ len(monthly_change),2)}")
        file.write("\n")
        file.write(f"Greatest Increase in Profits: {total_months[max_increase]}(${(str(max_increase))})")
        file.write("\n")
        file.write(f"Greatest Decrease in Profits: {total_months[max_decrease]}(${(str(max_decrease))})")