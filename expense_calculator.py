files = [open("sep16-oc16_2026/accountactivity (3).csv")]

transactions = {}

to_file = 1
if to_file:
    out_file = open("sep16-oc16_2026/totals.txt", 'x')

def print_switch(str):
    if to_file:
        print(str, file=out_file)
    else:
        print(str)

def find_max(data):
    highest = ""
    for key in data.keys():
        try:
            if data[key] > data[highest]:
                highest=key
        except KeyError:
            highest=key
    return highest

for file in files:
    line_count = 0
    for line in file:
        if line_count == 0:
            line_count += 1
            pass
        else:
            line_count += 1
            items = line.split(",")
            if items[0] != "" or items[0] != "chequing acct" or items[0] != "credit card":
                try:
                    data = (float(items[1]), items[2].rstrip('\n'))
                    if items[0] in transactions.keys():
                        transactions[items[0]].append(data)
                    else:
                        transactions[items[0]] = [data]
                except ValueError as err:
                    # print_switch(err)
                    # print_switch(items)
                    pass
                except IndexError as err:
                    pass

necessary = ["housing", "groceries", "transportation", "gym", "tuition"]

period_total = 0
saving_total = 0
income_total = 0
necessary_total = 0
unnecessary_total = 0
totals = {}
for key in transactions.keys():
    print_switch(f"----------{key}-------------")
    key_total = 0
    for line in (transactions[key]):
        key_total+=line[0]
        if key == "savings":
            saving_total+=line[0]
        elif key == "income":
            income_total+=line[0]
        elif (key != "school"):
            period_total+=line[0]
            if key in necessary:
                necessary_total+=line[0]
            else:
                unnecessary_total+=line[0]
            if (key != "housing"):
                totals[key]=key_total
        else:
            pass
        print_switch(line)
    print_switch(f"total for {key}: {key_total}")
print_switch(f"------totals for period:-----")
print_switch(f"total income: {round(income_total, 2)}")
print_switch(f"total spent: {round(period_total, 2)}")
print_switch(f"necessary expenses: {round(necessary_total, 2)}")
print_switch(f"unnecessary expenses: {round(unnecessary_total, 2)}")
print_switch(f"total saved: {round(saving_total, 2)}")
highest_key = find_max(totals)
print_switch(f"most spent: {highest_key}, {totals[highest_key]}")