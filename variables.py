played_lottery = True

url_lottery_guru = 'https://lotteryguru.com/ontario-lottery-results'

keno_logo_link = 'https://lotteryguru.com/pict/96850/ca-keno-2x-png'

data_url = 'https://github.com/Peterstangolis/lottery_tracking_dashboard/blob/main/data/keno_lottery_stats.csv?raw=true'

my_numbers = [
                [6, 18 , 67], [2, 14, 48], [16, 41, 66], [3, 6, 20 ], [11, 14, 52], [36, 46, 65],
                [5, 16, 64], [10, 19, 60], [12, 40, 68], [28, 31,54 ], [1, 13,42], [16, 18, 61]
              ]

pick_method = [None, "Algorithm", "App Quickpick", "Manual Picks"]

bet_amounts = [
               1.00, 1.00, 1.00, 1.00, 1.00, 1.00,
               1.00, 1.00, 1.00, 1.00, 1.00, 1.00
               ]

theory_used = "Based on Analysis"

keno_range = [x for x in range(1, 71)]

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

