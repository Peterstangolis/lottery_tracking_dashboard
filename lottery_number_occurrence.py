

def drawn_number_occurrences():
    # import libraries
    import pandas as pd
    import csv

    df = pd.read_csv('C:/Users/pstan/Documents/Continuing Education Data/lottery_tracking_dashboard/data/keno_lottery_stats.csv')

    keno_range = [x for x in range(1, 71)]

    list_of_numbers = []
    for i in range(len(df)):
        nums = df.iloc[i,:]["Numbers"]
        list = nums.split(",")
        for item in list:
            item = item.replace("[", "")
            item = item.replace("]", "").strip()
            list_of_numbers.append(int(item))

    number_occurrences = dict()
    for s in list_of_numbers:
        if str(s) not in number_occurrences.keys():
            number_occurrences[str(s)] = 1
        else:
            number_occurrences[str(s)] += 1

    number_occurrences_sorted = sorted(number_occurrences.items(), key=lambda x:x[1], reverse=True)
    number_occurrences_sorted = dict(number_occurrences_sorted)
    print(number_occurrences_sorted)
    numbers_drawn = number_occurrences_sorted.keys()

    numbers_not_drawn = []
    for num in keno_range:
        if num not in list_of_numbers:
            numbers_not_drawn.append(int(num))

    ## Save the occurrences
    w = csv.writer(open("data/lottery_number_occurrences.csv", "w"))

    for key, val in number_occurrences_sorted.items():

        w.writerow([key, val])

