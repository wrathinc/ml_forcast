import csv

with open('banking-batch.csv', mode='r') as infile:
    reader = csv.reader(infile)
  
    with open('banking-batchs.csv', mode='x') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[1] for rows in reader}
       



