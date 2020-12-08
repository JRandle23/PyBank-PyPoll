print("Financial Analysis")
print("...............................")

# import modules 
import os
import csv

#Create the file path for the csv
csvpath = 'PyBank/Resources/budget_data.csv'

#set lists to store data 
date = []
PLlist = []
change = []


#read the csvfile 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #set headerline as first row 
    header = next(csvreader)

    for row in csvreader:
        
        #append lists to store Profit/Losses and Dates 
        PLlist.append(int(row[1]))
        date.append(row[0])
    
    #calculates the total months included 
    for total_months in date:
        
        print("Total Months: ",len(date))

        break
    
    #calculates the net total of the PL column
    for total in PLlist:
        total = sum(PLlist)
        print("Total: ${}".format(total))

        break

    #calculate the average of the changes of the entire period 
    for x in range(len(PLlist) - 1):
        difference = PLlist[x+1] - PLlist[x]

        change.append(int(difference)) 

    average = float(sum(change)/85)
    print("Average Change: ${}".format(round(average, 2)))
       
    maximum = max(change)
    print("Greatest Increase in Profits: ", maximum)
    
    minimum = min(change)
    print("Greatest Decrease in Profits: ", minimum)
       

        


    

   
    
    
        

    



    

        
    

    

        

    
        
    
    


   
        

    


        



    
    

  








    



        
  
  
   
        








    
    





    




