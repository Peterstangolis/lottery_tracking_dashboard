## import variables
from variables import url_lottery_guru

## Import Libraries
import random
from random import choice

import datetime as dt

import requests
from bs4 import BeautifulSoup

import re

import pandas as pd


lottery_guru = requests.get(url_lottery_guru)
if lottery_guru.status_code != 200:
    break

soup_guru_2 = BS(lottery_guru.text, "lxml")

## Retrieve all the cards from the site
lottery_cards = soup_guru_2.find_all('div', class_ = 'lg-card lg-link')








# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')


