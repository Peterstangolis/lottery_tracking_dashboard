url_lottery_guru = 'https://lotteryguru.com/ontario-lottery-results'

keno_logo_link = 'https://lotteryguru.com/pict/96850/ca-keno-2x-png'

played_lottery = False

my_numbers = [
              [10,52,62],[49,31,16],[68, 53, 30], [36, 15, 46], [5, 66, 19],[5, 15, 31]
              #[], [], [], [], []
              ]

pick_method = [None, "Algorithm", "App Quickpick", "Manual Picks"]

bet_amounts = [
                2.00, 2.00, 2.00, 2.00, 2.00, 2.00
               #,1.00, 1.00, 1.00, 1.00, 1.00
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

