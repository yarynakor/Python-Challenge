import os
import csv
# Path to collect data from the UofA folder
csvfile = os.path.join('..', 'UofA', 'election_data.csv')

#define variables
total_votes = 0
candidates = {}
candidates_percent = {}
winner = ""
winner_count = 0

#Open file and leave out the header
with open(csvfile, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] in candidates.keys():
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

for key, value in candidates.items():
    candidates_percent[key] = round((value/total_votes)*100,2)

for key in candidates.keys():
    if candidates[key] > winner_count:
        winner = key
        winner_count = candidates[key]

print("Election Results")
print("-------------------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------------------")
for key, value in candidates.items():
    print(key + ": " + str(candidates_percent[key]) + "% (" + str(value) + ")")
print("-------------------------------------")
print("Winner: " + winner)
print("-------------------------------------")