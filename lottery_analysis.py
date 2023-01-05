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
    for n in range(len(df2)):
        if n != len(df2) - 1:
            before = df2.iloc[n]["Numbers_2"]
            after = df2.iloc[n + 1]["Numbers_2"]
            two_game_same = set(before) & set(after)
            repeated_numbers.append(sorted(two_game_same))
            two_game_diff = set(before).difference(after)
            numbers_for_game_selection = set(keno_range).difference(two_game_same)
            two_game_comparison.append(numbers_for_game_selection)

    ## Add the repeated numbers for 2 games in a row
    df2["Repeated Numbers"] = repeated_numbers

    ## Add the new column to the dataframe
    df2["Two_Game_Number_Comparison"] = two_game_comparison

    ## Add column to find the consecutive numbers of the numbers drawn
    df2["Consecutive_Numbers"] = df2["Numbers_2"].apply(consecutive_numbers_list)

    ## Save the data to a new csv file in the data folder
    df2.to_csv(
        'C:/Users/pstan/Documents/Continuing Education Data/lottery_tracking_dashboard/data/keno_lottery_analysis.csv',
        lineterminator='\n',
        index=False)