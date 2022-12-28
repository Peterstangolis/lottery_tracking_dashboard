## import variables
from variables import url_lottery_guru, keno_logo_link

## Import Libraries
import random
from random import choice

import datetime as dt

import requests
from bs4 import BeautifulSoup as BS
import lxml

import re
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
print(last_result_list)

next_result_date = draw_dates[1].text.strip()
next_result_list = next_result_date.split("\n")
print(next_result_list)


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

print(new_row)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':



