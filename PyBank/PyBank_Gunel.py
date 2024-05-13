# Modules
import csv

# Identify the path for the csv file
csvpath = "/Users/gunel/april/homework/03-Python/ds_module3_hm_3/PyBank/Resources/budget_data.csv"

#Add new  variables
month_count = 0
total_profit = 0
last_month_profit = 0
changes = []
month_changes = [] #list

# Use UTF-8 encoding and open csv file
with open(csvpath, encoding='UTF-8') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # Check the headers first. If we have the headers do the following:
        csv_header = next(csvreader)
        print(f"CSV Header: {csv_header}")
# Read each row of data after the header .Loop per row
        for row in csvreader:
            print(row)
            #For each row by adding 1 we are getting total. Count months
            month_count = month_count +1
            #total profit

            total_profit = total_profit + int(row[1])

        
            if(month_count == 1):
                 last_month_profit=int(row[1])
            else:
                 change = int(row[1])-last_month_profit
                 changes.append(change)
                 month_changes.append(row[0])

            #need to reset last_month_profit to be current month
                 last_month_profit=int(row[1])
        print(month_count)
        print(total_profit)
        print(len(changes))
        #Calculate max,min and avg
        avg_change = sum(changes) / len(changes)
        print(avg_change)
        max_change = max(changes)
        max_month_index = changes.index(max_change)
        max_month = month_changes[max_month_index]
        min_change = min(changes)
        min_month_index = changes.index(min_change)
        min_month = month_changes[min_month_index]

        print(max_change)
        print(max_month)

        print(min_change)
        print(min_month)

output = f"""Financial Analysis
      ----------------------------
      Total Months: {month_count}
      Total: ${total_profit}
      Average Change: ${round(avg_change, 2)}
      Greatest Increase in Profits: {max_month} (${max_change})
      Greatest Decrease in Profits: {min_month} (${min_change})"""
print(output)
with(open("output_pybank_Gunel.txt", 'w') as f):
        f.write(output)
