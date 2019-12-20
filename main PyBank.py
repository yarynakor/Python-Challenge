#import necessary modules
import os
import csv

cvspath = os.path.join("..", "UofA", "budget_data.csv")

totalMon = 0
Revenue_change = 0
avgRevenueChange = 0
great_inc_Date = "Date1"
great_increase = 0
great_dec_Date = "Date2"
great_decrease = 0
total_Rev_Change = 0
prev_Revenue = 0

#Read the budget_data.csv file
with open(cvspath) as csvfile:
    csvfile.readline()
    csvreader = csv.reader(csvfile, delimiter=',')

#loop through the data to collect the answers
    for row in csvreader:
       #Total Months, Revenue Change, Increase, Decrease
       Revenue_change = Revenue_change + int(row[1])
       totalMon = totalMon + 1 
       revIncrease = int(row[1]) - prev_Revenue
       Revenue_change = Revenue_change + revIncrease
       prev_Revenue =  int(row[1])
       if(revIncrease > great_increase):
           great_increase = revIncrease
           great_inc_Date = row[0]
            
       if(revIncrease < great_decrease):
           great_decrease = revIncrease
           great_dec_Date = row[0]

avgRevenueChange = round(Revenue_change/totalMon,2)

#print the outcomes
lines = []

lines.append("Financial Analysis")
lines.append("----------------------------")
lines.append("Total Months: "+str(totalMon))
lines.append("Total Revenue: $" + str(Revenue_change))
lines.append("Average Revenue Change: $"+str(avgRevenueChange))
lines.append("Greatest Increase in Revenue: "+great_inc_Date + " ($" + str(great_increase) +")")
lines.append("Greatest Decrease in Revenue: "+great_dec_Date + " ($" + str(great_decrease) +")")

for line in lines:
        print(line)