print("Financial Analysis")
print("...............................")

import os
import csv

csvpath = 'PyBank/Resources/budget_data.csv'

profits = []
change = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    header = next(csvreader)
    for row in csvreader:
         total_months = sum(1 for row in csvfile) + 1
    print("Total Months: {}".format(total_months))

    profits.append(row[1])
    





    



        
  
  
   
        








    
    





    




