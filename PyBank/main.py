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

        profits.append(int(row[1]))
        date.append(row[0])
    
    for total_months in date:
        
        print("Total Months: ", len(date))

        break
        
    for total in profits:
        total = sum(profits)
        print("Total: ${}".format(total))

        break
    
    for x in range(len(profits)):
        changes = profits[x] - profits[x-1]
        change.append(int(changes))
        average = sum(change)/85
        print("Average Change: ${}".format(round(average, 2)))

        break
    
    for y in range(len(change)):
        difference = 0
        for z in range(y + 1, len(change)):
            difference = change[z] - change[y]
        

    



    

        
    

    

        

    
        
    
    


   
        

    


        



    
    

  








    



        
  
  
   
        








    
    





    




