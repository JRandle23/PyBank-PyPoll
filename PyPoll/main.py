
import os
import csv

print("Election Results")
print("--------------------------")


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
    
    
    res = dict()
    for key in percentages:
        res[key] = "{0}%".format(round(percentages[key], 3))

    totals = dict(res)
    for k, v in counted_names:
        totals[k] = (totals[k], v if k in totals else v)
    
    for key, value in totals.items():
        formatted = ("{}: {}".format(key, value))
        print(formatted)

    print("--------------------------")

    import operator 
    winner = max(totals.items(), key=operator.itemgetter(1))[0]
    print("Winner: ", winner)
    
    output = (f"Election Results\n"
    f"--------------------------\n"
    f"Total Votes: {totalvotes}\n"
    f"--------------------------\n"
    f"{formatted}\n"
    f"--------------------------\n"
    f"Winner: {winner}\n")

    output_file = os.path.join('PyPoll/Analysis/output_text.txt')

    with open(output_file, 'w') as txtfile:
        txtfile.write(output)

    
    
 
   
   
    
    
    
    
    
    


   




    
   
   










