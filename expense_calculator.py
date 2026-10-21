files = [open("aug16-sep16_2026/accountactivity_fixed.csv")]

transactions = {}

to_file = 1
if to_file:
    out_file = open("aug16-sep16_2026/totals.txt", 'x')

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
            # Note: you might want to change 'or' to 'and' here depending on your CSV format!
            if items[0] != "" or items[0] != "chequing acct" or items[0] != "credit card":
                try:
                    data = (float(items[1]), items[2].rstrip('\n'))
                    if items[0] in transactions.keys():
                        transactions[items[0]].append(data)
                    else:
                        transactions[items[0]] = [data]
                except ValueError as err:
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
category_totals = {} # Added to track all totals cleanly for the table

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
    
    category_totals[key] = key_total # Save the raw total for the summary table
    print_switch(f"total for {key}: {key_total}")

# --- NEW TABLE CODE ---
print_switch("\n=======================================")
print_switch("         CATEGORY SUMMARY TABLE        ")
print_switch("=======================================")
print_switch(f"{'Category':<22} | {'Total':>12}")
print_switch("-" * 39)

print_switch("Necessary Expenses:")
for key, amt in category_totals.items():
    if key in necessary and key not in ["savings", "income", "school"]:
        print_switch(f"  {key:<20} | ${amt:>10.2f}")

print_switch("-" * 39)
print_switch("Unnecessary Expenses:")
for key, amt in category_totals.items():
    if key not in necessary and key not in ["savings", "income", "school"]:
        print_switch(f"  {key:<20} | ${amt:>10.2f}")
print_switch("=======================================\n")
# ----------------------

print_switch(f"------totals for period:-----")
print_switch(f"total income: {round(income_total, 2)}")
print_switch(f"total spent: {round(period_total, 2)}")
print_switch(f"necessary expenses: {round(necessary_total, 2)}")
print_switch(f"unnecessary expenses: {round(unnecessary_total, 2)}")
print_switch(f"total saved: {round(saving_total, 2)}")

highest_key = find_max(totals)
# Added a check just in case 'totals' is empty to prevent a KeyError
if highest_key: 
    print_switch(f"most spent: {highest_key}, {totals[highest_key]}")