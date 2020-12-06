print("Financial Analysis")
print("...............................")

import csv

csvpath = 'PyBank/Resources/budget_data.csv'

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvfile)
    total = 0
    for row in csvreader:
        total += float(row[1])
    print("Total: ${:,.2f}".format(total))





    




