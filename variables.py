played_lottery = True

url_lottery_guru = 'https://lotteryguru.com/ontario-lottery-results'

keno_logo_link = 'https://lotteryguru.com/pict/96850/ca-keno-2x-png'

data_url = 'https://github.com/Peterstangolis/lottery_tracking_dashboard/blob/main/data/keno_lottery_stats.csv?raw=true'

my_numbers = [
        [14, 43, 24, 29, 50],
        [10, 35, 53, 26, 63],
        [8, 13, 23, 62, 44],
        [29, 5, 39, 22, 66],
        [8, 69, 40, 30, 15],
        [25, 37, 55, 17, 7],
        [59, 54, 1, 21, 36, 24],
        [14, 35, 23, 44, 39, 69],
        [43, 10, 62, 29, 40, 25],
        [50, 4, 26, 44, 49, 55],
        [8, 24, 37, 54, 15, 65],
        [63, 67, 47, 28, 18, 36],
        [33, 20, 67, 62, 18, 55],
        [4, 16, 20, 39, 47, 56]
              ]

pick_method = [None, "Algorithm", "App Quickpick", "Manual Picks"]

bet_amounts = [
               1.00, 1.00, 1.00, 1.00, 1.00, 1.00,
               1.00, 1.00, 1.00, 1.00, 1.00, 1.00
             , 1.00
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

