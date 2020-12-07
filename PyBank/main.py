print("Financial Analysis")
print("...............................")

import os
import csv

csvpath = 'PyBank/Resources/budget_data.csv'

date = []
profits = []
change = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    for row in csvreader:

        date.append(row[0])
        profits.append(row[1])
    for total_months in date:
        print("Total Months: ", len(date) - 1)
        
        break

    


        



    
    

  








    



        
  
  
   
        








    
    





    




