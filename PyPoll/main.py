print("Election Results")
print("--------------------------")

import os
import csv

csvpath = 'PyPoll/Resources/election_data.csv'

candidates = []
voter_id = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    for row in csvreader:

        voter_id.append(row[0])
        candidates.append(row[2])

    for totalvotes in voter_id:
        totalvotes = len(voter_id)

        print("Total Votes: ", totalvotes)
        print("--------------------------")

        break
    
    from collections import Counter
    counted_names = Counter(candidates).items()
    
    percentages = {x: float(int(y)/len(candidates) * 100) for x, y in counted_names}
    
    for r in percentages.items():
        percentages = '{0:.2f}'.format


    totals = dict(percentages)
    for k, v in counted_names:
        totals[k] = [totals[k], v] if k in totals else v 
    
    print(totals)

    
    
    
    
 
   
   
    
    
    
    
    
    


   




    
   
   










