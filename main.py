## import variables
from variables import url_lottery_guru, keno_logo_link, played_lottery, \
    my_numbers, pick_method, bet_amounts, theory_used, data_url
from lottery_number_generator import list_of_nums
from lottery_number_occurrence import drawn_number_occurrences
from lottery_analysis import lot_analysis

## Import Libraries
import datetime as dt

import requests
from bs4 import BeautifulSoup as BS
import lxml
import pandas as pd

import time


def scrape_lottery_cards(url):
    lottery_guru = requests.get(url)

    if lottery_guru.status_code == 200:
        print("Scrape Function")

    soup_guru = BS(lottery_guru.text, "lxml")

    ## Retrieve all the cards from the site
    lottery_cards = soup_guru.find_all('div', class_ = 'lg-card lg-link')

    return lottery_cards

def keno_items():
    print("Keno Items")
    lottery_cards = scrape_lottery_cards(url_lottery_guru)

    results = dict()
    for n in [7,6]:

        keno_card = lottery_cards[n]
        ## Get the latest Keno Winning Numbers
        numbers = keno_card.find_all("ul", class_="lg-numbers")
        keno_numbers = list()
        for num in numbers[0].find_all("li"):
            keno_numbers.append(int(num.text))
            draw_dates = keno_card.find_all("div", class_="lg-time")
            last_result_date = draw_dates[0].text.strip()
            last_result_list = last_result_date.split("\n")
            next_result_date = draw_dates[1].text.strip()
            next_result_list = next_result_date.split("\n")
        results[f"card_{n}"] = [keno_numbers, last_result_list, next_result_list]


                # draw_dates = keno_card.find_all("div", class_="lg-time")
                # last_result_date = draw_dates[0].text.strip()
                # last_result_list = last_result_date.split("\n")
                # next_result_date = draw_dates[1].text.strip()
                # next_result_list = next_result_date.split("\n")

    keys = list(results.keys())
    if len(results[keys[0]][0]) == 20:
        return results[keys[0]][0], results[keys[0]][1], results[keys[0]][2]
    else:
        return results[keys[1]][0], results[keys[1]][1], results[keys[1]][2]


def matched_numbers(my_picks, played_lottery):
    print("Matched Numbers")

    keno_numbers, last_result_list, next_result_list = keno_items()

    if played_lottery:

        matched_picks_one = [x for x in my_picks[0] if x in keno_numbers]
        matched_picks_two = [x for x in my_picks[1] if x in keno_numbers]
        matched_picks_three = [x for x in my_picks[2] if x in keno_numbers]
        matched_picks_four = [x for x in my_picks[3] if x in keno_numbers]
        matched_picks_five = [x for x in my_picks[4] if x in keno_numbers]
        matched_picks_six = [x for x in my_picks[5] if x in keno_numbers]
        matched_picks_seven = [x for x in my_picks[6] if x in keno_numbers]
        matched_picks_eight = [x for x in my_picks[7] if x in keno_numbers]
        matched_picks_nine = [x for x in my_picks[8] if x in keno_numbers]
        matched_picks_ten = [x for x in my_picks[9] if x in keno_numbers]
        matched_picks_eleven = [x for x in my_picks[10] if x in keno_numbers]
        matched_picks_twelve = [x for x in my_picks[11] if x in keno_numbers]

        matched_vs_picked_one = f'{len(matched_picks_one)}/{len(my_picks[0])}'
        matched_vs_picked_two = f'{len(matched_picks_two)}/{len(my_picks[1])}'
        matched_vs_picked_three = f'{len(matched_picks_three)}/{len(my_picks[2])}'
        matched_vs_picked_four = f'{len(matched_picks_four)}/{len(my_picks[3])}'
        matched_vs_picked_five = f'{len(matched_picks_five)}/{len(my_picks[4])}'
        matched_vs_picked_six = f'{len(matched_picks_six)}/{len(my_picks[5])}'
        matched_vs_picked_seven = f'{len(matched_picks_seven)}/{len(my_picks[6])}'
        matched_vs_picked_eight = f'{len(matched_picks_eight)}/{len(my_picks[7])}'
        matched_vs_picked_nine = f'{len(matched_picks_nine)}/{len(my_picks[8])}'
        matched_vs_picked_ten = f'{len(matched_picks_ten)}/{len(my_picks[9])}'
        matched_vs_picked_eleven = f'{len(matched_picks_eleven)}/{len(my_picks[10])}'
        matched_vs_picked_twelve = f'{len(matched_picks_twelve)}/{len(my_picks[11])}'

    else:
        matched_picks_one = None
        matched_picks_two = None
        matched_picks_three = None
        matched_picks_four = None
        matched_picks_five = None
        matched_picks_six = None
        matched_picks_seven = None
        matched_picks_eight = None
        matched_picks_nine = None
        matched_picks_ten = None
        matched_picks_eleven = None
        matched_picks_twelve = None

        matched_vs_picked_one = None
        matched_vs_picked_two = None
        matched_vs_picked_three = None
        matched_vs_picked_four = None
        matched_vs_picked_five = None
        matched_vs_picked_six = None
        matched_vs_picked_seven = None
        matched_vs_picked_eight = None
        matched_vs_picked_nine = None
        matched_vs_picked_ten = None
        matched_vs_picked_eleven = None
        matched_vs_picked_twelve = None

    return keno_numbers, last_result_list, matched_picks_one, matched_picks_two, matched_picks_three, matched_picks_four, matched_picks_five, matched_picks_six, \
           matched_picks_seven, matched_picks_eight, matched_picks_nine, matched_picks_ten, matched_picks_eleven, matched_picks_twelve, \
           matched_vs_picked_one, matched_vs_picked_two, matched_vs_picked_three, matched_vs_picked_four, matched_vs_picked_five, matched_vs_picked_six, matched_vs_picked_seven,  \
           matched_vs_picked_eight, matched_vs_picked_nine, matched_vs_picked_ten, matched_vs_picked_eleven, matched_vs_picked_twelve


## New Row to Add to CSV file
def new_row_to_csv(played_lottery, bet_amounts, pick_method, my_picks, theory_used):
    print("New Row")
    keno_numbers, last_result_list, matched_picks_one, matched_picks_two, matched_picks_three, matched_picks_four, matched_picks_five, matched_picks_six, \
    matched_picks_seven, matched_picks_eight, matched_picks_nine, matched_picks_ten, matched_picks_eleven, matched_picks_twelve,  \
    matched_vs_picked_one, matched_vs_picked_two, matched_vs_picked_three, matched_vs_picked_four, matched_vs_picked_five, matched_vs_picked_six, \
    matched_vs_picked_seven, matched_vs_picked_eight, matched_vs_picked_nine, matched_vs_picked_ten, matched_vs_picked_eleven, matched_vs_picked_twelve \
        = matched_numbers(my_picks=my_picks, played_lottery=played_lottery)
    # matched_picks_six, matched_picks_seven, matched_picks_eight, matched_picks_nine, matched_picks_ten, matched_picks_eleven, matched_picks_twelve  \
    # matched_vs_picked_six, matched_vs_picked_seven, matched_vs_picked_eight, matched_vs_picked_nine, matched_vs_picked_ten, matched_vs_picked_eleven, matched_vs_picked_twelve \

    new_row = {'Weekday' : last_result_list[2] ,
               'Draw Date' : last_result_list[3],
               'Time of day' : last_result_list[-1] ,
               'Numbers' : keno_numbers,
               'Played' : played_lottery,
               'My Numbers': my_numbers,
               'Bet Amounts': bet_amounts,
               'Matched Numbers' : [
                                  matched_picks_one
                                , matched_picks_two
                                , matched_picks_three
                                , matched_picks_four
                                , matched_picks_five
                                , matched_picks_six
                                , matched_picks_seven
                                , matched_picks_eight
                                , matched_picks_nine
                                , matched_picks_ten
                                , matched_picks_eleven
                                , matched_picks_twelve
                                    ],
               'Correct vs Picked' : [
                                  matched_vs_picked_one
                                , matched_vs_picked_two
                                , matched_vs_picked_three
                                , matched_vs_picked_four
                                , matched_vs_picked_five
                                , matched_vs_picked_six
                                , matched_vs_picked_seven
                                , matched_vs_picked_eight
                                , matched_vs_picked_nine
                                , matched_vs_picked_ten
                                , matched_vs_picked_eleven
                                , matched_vs_picked_twelve
                                      ],
               'Pick Method' : pick_method,
               'Theory Used' : theory_used
               }

    return new_row


def update_csv(played_lottery, bet_amounts, pick_method, my_picks, theory_used):

    new_row = new_row_to_csv(played_lottery=played_lottery, bet_amounts=bet_amounts, pick_method=pick_method, my_picks=my_numbers, theory_used=theory_used)

    keno_numbers, last_result_list, matched_picks_one, matched_picks_two, matched_picks_three, matched_picks_four, matched_picks_five, matched_picks_six, \
    matched_picks_seven, matched_picks_eight, matched_picks_nine, matched_picks_ten, matched_picks_eleven, matched_picks_twelve,  \
    matched_vs_picked_one, matched_vs_picked_two, matched_vs_picked_three, matched_vs_picked_four, matched_vs_picked_five, matched_vs_picked_six, \
    matched_vs_picked_seven, matched_vs_picked_eight, matched_vs_picked_nine, matched_vs_picked_ten, matched_vs_picked_eleven, matched_vs_picked_twelve \
        = matched_numbers(my_picks=my_picks, played_lottery=played_lottery)
    # matched_picks_six, matched_picks_seven, matched_picks_eight, matched_picks_nine, matched_picks_ten, matched_picks_eleven, matched_picks_twelve  \
    # matched_vs_picked_six, matched_vs_picked_seven, matched_vs_picked_eight, matched_vs_picked_nine, matched_vs_picked_ten, matched_vs_picked_eleven, matched_vs_picked_twelve

    keno_df = pd.read_csv('C:/Users/pstan/Documents/Continuing Education Data/lottery_tracking_dashboard/data/keno_lottery_stats.csv')

    last_winning_numbers = keno_df["Numbers"].iloc[-1]
    last_winning_numbers = last_winning_numbers.replace("[", "", 3)
    last_winning_numbers = last_winning_numbers.replace("]", "", 2)
    last_winning_numbers = [int(e) for e in last_winning_numbers.split(",")]
    print(keno_df["Draw Date"].tail(1), keno_df["Time of day"].tail(1))


    ## Add the new row of Keno numbers to the file if the last numbers do not equal the winning numbers
    if last_winning_numbers == keno_numbers:
        print("No Draw Yet")
    else:
        print("Next lottery draw has occurred")
        keno_df = keno_df.append(new_row, ignore_index=True)

        ## Save the updated file to the data folder
        keno_df.to_csv('C:/Users/pstan/Documents/Continuing Education Data/lottery_tracking_dashboard/data/keno_lottery_stats.csv',
                       lineterminator='\n',
                       index=False)



if __name__ == '__main__':
    update_csv(played_lottery=played_lottery, bet_amounts=bet_amounts, pick_method=pick_method[0], my_picks=my_numbers, theory_used=theory_used)
    drawn_number_occurrences()
    lot_analysis(data_url)
    time.sleep(6)



