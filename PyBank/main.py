print("Financial Analysis")
print("...............................")

import csv

csvpath = 'PyBank/Resources/budget_data.csv'

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    for row in csvreader:
        total_months = sum(1 for row in csvfile)
    print("Total Months: {}".format(total_months))

    
    for row in csvreader:
        total = sum(1 for row in csvfile )
    print("Total: ${}".format(total))





    




