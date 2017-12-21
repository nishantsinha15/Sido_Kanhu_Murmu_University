import csv
# Read CSV file
with open('s.csv', 'r') as fp:
    reader = csv.reader(fp, delimiter=',', quotechar='"')
    # next(reader, None)  # skip the headers
    data_read = [row for row in reader]
x = 0
dic = {}
for row in data_read:
    row.pop(0)
data_read.pop(2)

header = data_read[0]

data = data_read
data.pop(0)

for i in header:
    dic[i] = {}
    dic[i][''] = 0
    dic[i]['0'] = 0
    dic[i]['1'] = 0
    dic[i]['2'] = 0
    dic[i]['3'] = 0
    dic[i]['x'] = 0

# for i in dic.keys():
#     print i, dic[i]

for i in range(len(header)):
    for row in data:
        if row[i] in dic[header[i]]:
            dic[header[i]][row[i]] += 1
        else:
            dic[header[i]]['x'] += 1

# for i in dic.keys():
#     print i, dic[i]

x = dic.keys()
x.sort()

ans = []
for i in x:
    temp = []
    temp.append(i)
    # temp.append(dic[i][''])
    # temp.append(dic[i]['0'])
    temp.append(dic[i]['1'])
    temp.append(dic[i]['2'])
    # temp.append(dic[i]['3'])
    # temp.append(dic[i]['x'])
    ans.append(temp)
    print temp

with open('test.csv', 'w') as fp:
    writer = csv.writer(fp, delimiter=',')
    writer.writerow(["Question","1", "2"])  # write header
    writer.writerows(ans)