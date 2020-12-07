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
    
    def sum_of_list(numbers):
        total = 0
        for val in numbers:
            total = total + val
        return total 
    
    print("Total: ", sum_of_list(profits))



   
        

    


        



    
    

  








    



        
  
  
   
        








    
    





    




