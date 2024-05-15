#Modules
import csv

# Identify the path for the csv file
csvpath = "Resources/election_data.csv"

#Add new  variables
vote_count = 0
candidate_dic = {}
max_cand = ""
max_votes = 0

# Use UTF-8 encoding and open csv file
with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # Check the headers first. If we have the headers do the following:
        csv_header = next(csvreader)
        print(f"CSV Header: {csv_header}")
# Read each row of data after the header .Loop per row
        for row in csvreader:
            #print(row)
            #For each row by adding 1 we are getting total count. Count votes
            vote_count += 1
            #Creeate a dictonary and add the followings:
            row_candidate = row[2]
            if row_candidate in candidate_dic.keys():
                candidate_dic[row_candidate] += 1
            else:
                 candidate_dic[row_candidate] = 1          



# create our output
output = f"""Election Results
-------------------------
Total Votes: {vote_count}
-------------------------\n"""

for candidate in candidate_dic.keys():
    # find votes
    votes = candidate_dic[candidate]
    perc = (votes / vote_count) * 100

    line = f"{candidate}: {round(perc, 3)}% ({votes})\n"
    output += line

    # find the max value from the dictionary
    if votes > max_votes:
        max_cand = candidate
        max_votes = votes

last_line = f"""-------------------------
Winner: {max_cand}
-------------------------"""
output += last_line

print(output)
with open("output_PyPoll_Gunel.txt", 'w') as f:
    f.write(output)


