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

    #calculate the changes in PL of the changes of the entire period 
    for x in range(len(PLlist) - 1):
        difference = PLlist[x+1] - PLlist[x]

        #add changes calculate to the change list 
        change.append(int(difference))
        date.append(row[0]) 

    #calculate the average of the changes
    average = float(sum(change)/85)
    print("Average Change: ${}".format(round(average, 2)))

    #find the greatest increases in profits   
    maximum = max(change)
    index = change.index(1926159)
    for i, (b,a) in enumerate(zip(date, change)):
        index_1 = index + 1

        maxvaluedate = date[index_1]
    formatted_maximum = "${:}".format(maximum)

    #find the greatest decrease in profits 
    minimum = min(change)
    index_m = change.index(-2196167)
    for j, (c,d) in enumerate(zip(date, change)):
        index_2 = index_m + 1
        minvaluedate = date[index_2]
    formatted_minimum = "${:}".format(minimum)
    print("Greatest Increase in Profits: ", maxvaluedate, formatted_maximum)
    print("Greatest Decrease in Profits: ", minvaluedate, formatted_minimum)
       

        


    

   
    
    
        

    



    

        
    

    

        

    
        
    
    


   
        

    


        



    
    

  








    



        
  
  
   
        








    
    





    




