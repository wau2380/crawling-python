import csv
max_temp = -999
max_date = ''

f = open('temper3.csv')
data = csv.reader(f)
header = next(data)
for row in data :
    if row[-1] == '':
        row[-1] = -9999
    else:
        row[-1] = float(row[-1]) 
        
    if max_temp < row[-1]:
        max_date = row[0]
        max_temp = row[-1]
        
f.close()
print(max_date, max_temp)