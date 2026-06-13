import pandas as pd

df = pd.read_csv('/Users/jlam/Downloads/bobin/texas.csv');

df = df.fillna('N/A')

masterlist = []
count = 0
error = 0
for row in df.itertuples():
    # add row to a giant list
    newlist = []
    for item in row:
        newlist.append(item)
        if item == "ERROR":
            error = 1
    if error != 1:
        masterlist.append(newlist)

print(masterlist)