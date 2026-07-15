import pandas as pd

def one_spreadsheet(filename):
    df = pd.read_csv(filename)
    df = df.fillna('N/A')

    result = ""
    visited = []
    visited.append("ALABAMA")
    state = "ALABAMA"
    rows_left = True

    newly_added = []
    terminated = []
    existing = []

    for row in df.itertuples():
        if rows_left:
            if row[1] not in visited:
                # add old state to the results
                result += f'const {state}_new = {newly_added};\n'
                result += f'const {state}_terminated = {terminated};\n'
                result += f'const {state}_existing = {existing};\n'

                newly_added = []
                terminated = []
                existing = []

                # update new state
                state = row[1]

                # add new state to visited, so it becomes the old state
                visited.append(state)

# build new list
            count = 0
            error = 0
                # build each row as a list of items

            new_row = []
            for item in row:
                new_row.append(item)
                if item == "ERROR":
                    error = 1
                if item == "N/A":
                    count += 1
            if error != 1 and count < 13:
                if new_row[14] == "Terminated":
                    terminated.append(new_row)
                elif new_row[14] == "Newly_added":
                    newly_added.append(new_row)
                else:
                    existing.append(new_row)
            else: 
                rows_left = False
                result += f'const {state}_new = {newly_added};\n'
                result += f'const {state}_terminated = {terminated};\n'
                result += f'const {state}_existing = {existing};\n'
    
    state_list = "["
    for state in visited:
        state_list += f'...{state}, '
    state_list = state_list[:-2]
    state_list += "]"
    print(result)
    print(state_list)
    


def per_spreadsheet(states: list):

    result = ""

    for state in states: 
        filename = f'/Users/jlam/Downloads/bobin/{state}.csv'
        df = pd.read_csv(filename)
        df = df.fillna('N/A')

        newly_added = []
        terminated = []
        existing = []

        count = 0
        error = 0
        for row in df.itertuples():
            # build each row as a list of items
            new_row = []
            for item in row:
                new_row.append(item)
                if item == "ERROR":
                    error = 1
                if item == "N/A":
                    count += 1
            if error != 1 and count < 8:
                if new_row[14] == "Terminated":
                    terminated.append(new_row)
                elif new_row[14] == "Newly_added":
                    newly_added.append(new_row)
                else:
                    existing.append(new_row)

        result += f'const {state}_new = {newly_added};\n'
        result += f'const {state}_terminated = {terminated};\n'
        result += f'const {state}_existing = {existing};\n'

    print(result)


one_spreadsheet("/Users/jlam/Downloads/bobin/all_071426.csv")
