## import variables
from variables import url_lottery_guru, keno_logo_link

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

keno_card = lottery_cards[7]

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


new_row = {'Weekday' : last_result_list[2] ,
           'Draw Date' : last_result_list[3],
           'Time of day' : last_result_list[-1] ,
           'Numbers' : keno_numbers,
           'Played' : False,
           'My Numbers': None
           }


keno_df = pd.read_csv('data/keno_lottery_stats.csv')
print(keno_df.head())

last_winning_numbers = keno_df.loc[-1:]["Numbers"][0]
last_winning_numbers= last_winning_numbers.replace("[", "", 3)
last_winning_numbers = last_winning_numbers.replace("]", "", 2)
last_winning_numbers = [int(e) for e in last_winning_numbers.split(",")]
print(last_winning_numbers)
print(keno_numbers)


## Add the new row of Keno numbers to the file if the last numbers do not equal the winning numbers
if last_winning_numbers == keno_numbers:
    print("No Draw Yet")
else:
    print("Next lottery draw has occurred")
    keno_df = keno_df.append(new_row, ignore_index=True)

    ## Save the updated file to the data folder
    keno_df.to_csv('data/keno_lottery_stats.csv', index=False)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(" ")



