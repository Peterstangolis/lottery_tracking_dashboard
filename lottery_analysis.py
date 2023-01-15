import pandas as pd

from variables import keno_range

## Convert the list of strings into lists of integers / floats
def list_conversion(l):
    if isinstance(l, int):
        return l
    else:
        new_list = []
        l2 = l.split(',')
        for item in l2:
            i = item.replace('[','').replace(']','').strip()
            if not i:
                i = i
            else:
                try:
                    i = int(i)
                except:
                    i = float(i)
            new_list.append(i)
        return new_list

## Get the total amount bet for the played draw
def bet_totals(x):
    import math
    if x != 0 and len(x) > 1:
        total = math.fsum(x)
        return total
    else:
        total = 0
        return total

## Get a list of odd vs even numbers for each draw
def odd_vs_even(x):
    # list_of_draws = df2["Numbers_2"].values
    # for n, list in enumerate(list_of_draws):
    odds_evens = dict()
    odd_even = ["even" if i % 2 == 0 else "odd" for i in x]
    odds = odd_even.count("odd")
    evens = odd_even.count("even")
    odds_evens["odds"] = odds
    odds_evens["evens"] = evens

    return odds_evens

## Get a list of consecutive numbers in the lottery draw
def consecutive_numbers_list(l):

    consecutive_numbers = []
    for i, n in enumerate(l):
        if i == len(l)-1:
            continue
        else:
            diff = n - l[i+1]
            if abs(diff) == 1:
                cs = [l[i+1], n]
                consecutive_numbers.append(cs)
    return consecutive_numbers

## Return the numbers over 35 vs under
def over_under(l):
    over_under_35 = {
        "over_35": 0,
        "under_35": 0
    }

    for n in l:
        if n > 34:
            over_under_35["over_35"] += 1
        else:
            over_under_35["under_35"] += 1

    return over_under_35

## Return a dictionary that lists the numbers that fall into division of 10
def tens_category(l):
    tens = {
        '0': 0,
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6' : 0,
        '7' : 0
    }

    for n in l:
        if len(str(n)) == 1:
            tens['0'] += 1
        else:
            start = str(n)[0]
            tens[start] += 1
    return tens

## Correct vs Incorrect picks
def correct_vs_incorrect(df):
    correct_incorrect = []
    for i in range(len(df)):
        if df.iloc[i]["Played"] == True:
            my_picks = df.iloc[i]["My_Numbers_2"]
            #my_picks = list_conversion(my_picks)
            last_picks = df.iloc[i]["Numbers_2"]
            #last_picks = list_conversion(last_picks)
            correct = set(last_picks) & set(my_picks)
            correct_incorrect.append(round(len(correct) / len(my_picks), 3))
        else:
            correct_incorrect.append(0)
    return correct_incorrect

## Sum of Numbers
def sum_of_picks(l):
    import math
    return sum(l)

## Break down the numbers drawn in more groupings
def numbers_grouping(l):
    from variables import numbers_breakdown
    l = list_conversion(l)
    num_groups = {
    "ODD_1_19" : 0,
    "EVEN_2_18" : 0,
    "ODD_21_35" : 0,
    "EVEN_20_34" : 0,
    "ODD_37_51" : 0,
    "EVEN_36_52" : 0,
    "ODD_53_69" : 0,
    "EVEN_54_70" : 0
    }
    for num in l:
        for k,v in numbers_breakdown.items():
            if num in v:
                if k not in num_groups.keys():
                    num_groups[k] = 1
                else:
                    num_groups[k] += 1
            else:
                continue
    return num_groups



## Creating a new dataframe with general lottery analysis
def lot_analysis(url):
    import math
    from numpy import nan

    df = pd.read_csv(url,
                     index_col=0
                     )

    df.reset_index(inplace=True)
    df2 = df.fillna(0)
    df2["Draw Date"] = pd.to_datetime(df2["Draw Date"])

    df2["Bet_Amounts_2"] = df2["Bet Amounts"].apply(list_conversion)
    df2["Numbers_2"] = df2["Numbers"].apply(list_conversion)
    df2["My_Numbers_2"] = df2["My Numbers"].apply(list_conversion)

    df2["Bet_Totals"] = df2["Bet_Amounts_2"].apply(bet_totals)

    df2["Odds_vs_Evens"] = df2["Numbers_2"].apply(odd_vs_even)

    ## Create a column comparing numbers repeating in two consecutive draws and returning
    # a list of numbers that have not been repeat to choose from
    two_game_comparison = [None, ]
    repeated_numbers = [None, ]
    drawn_once = [None, ]
    for n in range(len(df2)):
        if n != len(df2) - 1:
            before = df2.iloc[n]["Numbers_2"]
            after = df2.iloc[n + 1]["Numbers_2"]
            two_game_same = set(before) & set(after)
            repeated_numbers.append(sorted(two_game_same))
            two_game_diff = set(before).difference(after)
            numbers_for_game_selection = set(keno_range).difference(two_game_same)
            two_game_comparison.append(numbers_for_game_selection)
            numbers_drawn_once = set(after).difference(two_game_same)
            drawn_once.append(sorted(numbers_drawn_once))



    ## Add the repeated numbers for 2 games in a row
    df2["Repeated Numbers"] = repeated_numbers

    ## Add set of numbers drawn once
    df2["Numbers Not Repeated"] = drawn_once

    ## Add the new column to the dataframe
    df2["Two_Game_Number_Comparison"] = two_game_comparison

    ## Add column to find the consecutive numbers of the numbers drawn
    df2["Consecutive_Numbers"] = df2["Numbers_2"].apply(consecutive_numbers_list)

    ## Over / under 35 totals
    df2["Over_Under_35"] = df2["Numbers_2"].apply(over_under)

    ## Tens Category breakdown
    df2["Tens_Category"] = df2["Numbers_2"].apply(tens_category)

    ## Numbers Groupings
    df2["Number Groupings"] = df2["Numbers"].apply(numbers_grouping)

    correct_perc = correct_vs_incorrect(df2)
    df2["Correct_vs_Incorrect"] = correct_perc

    df2["Sum_of_picks"] = df2["Numbers_2"].apply(sum_of_picks)

    ## Save the data to a new csv file in the data folder
    df2.to_csv(
        'C:/Users/pstan/Documents/Continuing Education Data/lottery_tracking_dashboard/data/keno_lottery_analysis.csv',
        lineterminator='\n',
        index=False)