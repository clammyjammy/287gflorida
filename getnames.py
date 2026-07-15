import pandas as pd

states = ["arkansas", "alabama", "alaska", "colorado", "georgia"]

result = ""
for state in states: 
    filename = f'/Users/jlam/Downloads/bobin/{state}.csv'
    df = pd.read_csv(filename);

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
            if item == "N/A":
                count += 1
        if error != 1 and count < 7:
            masterlist.append(newlist)

    result += f'{state} = {masterlist}\n'

print(result)