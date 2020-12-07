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
    
    header = next(csvreader)

    for row in csvreader:

        date.append(row[0])
        profits.append(row[1])
    
    for total_months in date:
        print("Total Months: ", len(date))
        
        break

    total = 0

    for numbers in range(0, len(profits)):
        total = total + profits[numbers]
        print("Total: ", total)

        break
        



   
        

    


        



    
    

  








    



        
  
  
   
        








    
    





    




