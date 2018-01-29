import csv
import plotly.plotly as py
import plotly.graph_objs as go

# Read CSV file
with open('students.csv', 'r') as fp:
    reader = csv.reader(fp, delimiter=',', quotechar='"')
    # next(reader, None)  # skip the headers
    data_read = [row for row in reader]
x = 0
for row in data_read:
    row.pop(0)

header = data_read[0]
data = data_read
data.pop(0)

dic = {}
for i in header:
    dic[i] = {}
    dic[i][''] = 0
    dic[i]['0'] = 0
    dic[i]['1'] = 0
    dic[i]['2'] = 0
    dic[i]['3'] = 0
    dic[i]['x'] = 0

for i in range(len(header)):
    for row in data:
        if row[i] in dic[header[i]]:
            dic[header[i]][row[i]] += 1
        else:
            dic[header[i]]['x'] += 1

x = list(dic.keys())
x.sort()

ans = []
labels = ['Yes(1)', 'No(2)', 'Other']

# Sent files till 12
for j in range(12):
    i = x[j]
    temp = []
    # temp.append(i)
    # temp.append(dic[i][''])
    # temp.append(dic[i]['0'])
    temp.append(dic[i]['1'])
    temp.append(dic[i]['2'])
    temp.append(dic[i]['3'] + dic[i]['x'] + dic[i][''] )
    trace = go.Pie( labels = labels, values = temp )
    py.plot([trace], filename = str("Students_" + i) )
    # temp.append(dic[i]['x'])
    # ans.append(temp)
    print(temp)
#
# with open('output.csv', 'w') as fp:
#     writer = csv.writer(fp, delimiter=',')
#     writer.writerow(["Question","1", "2", "Others"])  # write header
#     writer.writerows(ans)
#
