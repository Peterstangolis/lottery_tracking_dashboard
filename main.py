## import variables
from variables import url_lottery_guru, keno_logo_link
from lottery_number_generator import list_of_nums

## Import Libraries
import datetime as dt

import requests
from bs4 import BeautifulSoup as BS
import lxml
import pandas as pd


lottery_guru = requests.get(url_lottery_guru)

if lottery_guru.status_code == 200:
    print("Authorized")

soup_guru_2 = BS(lottery_guru.text, "lxml")

## Retrieve all the cards from the site
lottery_cards = soup_guru_2.find_all('div', class_ = 'lg-card lg-link')

keno_card = lottery_cards[6]

draw_dates = keno_card.find_all("div", class_="lg-time")

last_result_date = draw_dates[0].text.strip()
last_result_list = last_result_date.split("\n")

next_result_date = draw_dates[1].text.strip()
next_result_list = next_result_date.split("\n")


## Get the latest Keno Winning Numbers
nums = keno_card.find_all("ul", class_="lg-numbers")

keno_numbers = list()
for n in nums[0].find_all("li"):
    keno_numbers.append(int(n.text))

print(keno_numbers)

played_lottery = False
if played_lottery == True:
    my_numbers = [[32,40,42],[22,27,40]]
    bet_amount = [2.00, 2.00]

    matched_picks_one = [x for x in my_numbers[0] if x in keno_numbers]
    matched_picks_two = [x for x in my_numbers[1] if x in keno_numbers]
    #matched_picks_three = [x for x in my_numbers[2] if x in keno_numbers]
    #matched_picks_four = [x for x in my_numbers[3] if x in keno_numbers]
    #matched_picks_five = [x for x in my_numbers[4] if x in keno_numbers]

    matched_vs_picked_one = f'{len(matched_picks_one)}/{len(my_numbers[0])}'
    matched_vs_picked_two = f'{len(matched_picks_two)}/{len(my_numbers[1])}'
    #matched_vs_picked_three = f'{len(matched_picks_three)}/{len(my_numbers[2])}'
    #matched_vs_picked_four = f'{len(matched_picks_four)}/{len(my_numbers[3])}'
    #matched_vs_picked_five = f'{len(matched_picks_five)}/{len(my_numbers[4])}'

    pick_method = "App Quickpick"

else:
    my_numbers = None
    bet_amount = None
    matched_picks_one = None
    matched_picks_two = None
    matched_picks_three = None
    matched_vs_picked_one = None
    matched_vs_picked_two = None
    matched_vs_picked_three = None

    pick_method = None

## New Row to Add to CSV file
new_row = {'Weekday' : last_result_list[2] ,
           'Draw Date' : last_result_list[3],
           'Time of day' : last_result_list[-1] ,
           'Numbers' : keno_numbers,
           'Played' : played_lottery,
           'My Numbers': my_numbers,
           'Bet Amounts': bet_amount,
           'Matched Numbers' : [matched_picks_one, matched_picks_two,
                                #matched_picks_three, matched_picks_four, matched_picks_five
                                ],
           'Correct vs Picked' : [matched_vs_picked_one, matched_vs_picked_two
               #, matched_vs_picked_three, matched_vs_picked_four, matched_vs_picked_five
                                  ],
           'Pick Method' : pick_method
           }


keno_df = pd.read_csv('data/keno_lottery_stats.csv')

last_winning_numbers = keno_df["Numbers"].iloc[-1]
print(last_winning_numbers)
last_winning_numbers = last_winning_numbers.replace("[", "", 3)
last_winning_numbers = last_winning_numbers.replace("]", "", 2)
last_winning_numbers = [int(e) for e in last_winning_numbers.split(",")]
print(last_winning_numbers)
print(keno_df["Draw Date"].tail(1))

print()
print(new_row)



## Add the new row of Keno numbers to the file if the last numbers do not equal the winning numbers
if last_winning_numbers == keno_numbers:
    print("No Draw Yet")
else:
    print("Next lottery draw has occurred")
    keno_df = keno_df.append(new_row, ignore_index=True)

    ## Save the updated file to the data folder
    keno_df.to_csv('data/keno_lottery_stats.csv', index=False)




if __name__ == '__main__':
    print(" ")



