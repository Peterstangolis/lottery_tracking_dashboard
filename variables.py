url_lottery_guru = 'https://lotteryguru.com/ontario-lottery-results'

keno_logo_link = 'https://lotteryguru.com/pict/96850/ca-keno-2x-png'

played_lottery = True

my_numbers = [[23, 30, 40],[6, 32, 61],[6, 17, 55], [4, 23, 57], [31, 54, 59], [3, 28, 54], [14, 29, 42], [2, 3, 36], [13, 36, 44], [1, 27, 52]]

pick_method = [None, "Algorithm", "App Quickpick"]

bet_amounts = [
                1.00, 1.00, 1.00, 1.00, 1.00
               ,1.00, 1.00, 1.00, 1.00, 1.00
               ]

list_of_lotteries = {
    "Lotto 6/49": {"selections": 6,
                   "range_of_nums": [1, 49]
                   },

    "Lotto Max": {"selections": 7,
                  "range_of_nums": [1, 50]
                  },
    "Daily Grand": {"selections": [5, 1],
                    "range_of_numbs": [[1, 49], [1, 7]]
                    },
    "Daily Keno": {"selections": [2, 3, 4, 5, 6, 7, 8, 9, 10],
                   "range_of_nums": [1, 70],
                   "bet_amount": [1.00, 2.00, 5.00, 10.00],
                   "draw_occurence": "daily",
                   "draw_time": ["14:00", "22:30"],
                   "time_zone": "Eastern Time"
                   },
    "Ontario 49": {"selections": 6,
                   "range_of_nums": [1, 40]
                   }
}

