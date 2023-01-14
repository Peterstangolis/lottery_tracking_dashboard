played_lottery = True

url_lottery_guru = 'https://lotteryguru.com/ontario-lottery-results'

keno_logo_link = 'https://lotteryguru.com/pict/96850/ca-keno-2x-png'

data_url = 'https://github.com/Peterstangolis/lottery_tracking_dashboard/blob/main/data/keno_lottery_stats.csv?raw=true'

data_analysis_url =  'https://github.com/Peterstangolis/lottery_tracking_dashboard/blob/main/data/keno_lottery_analysis.csv?raw=true'

lott_analysis_csv = 'C:/Users/pstan/Documents/Continuing Education Data/lottery_tracking_dashboard/data/keno_lottery_analysis.csv'
lott_stats_csv = 'C:/Users/pstan/Documents/Continuing Education Data/lottery_tracking_dashboard/data/keno_lottery_stats.csv'


my_numbers = [
        [6, 23, 34, 50, 61],
        [4, 24, 27, 31, 52],
        [7, 21, 30, 38, 60],
        [8, 18, 31, 45, 54],
        [11, 19, 34, 63, 64],
        [6, 24, 30, 45, 63],
        [4, 23, 38, 63, 45],
        [7, 34, 52, 18, 64],
        [8, 21, 24, 52, 65],
        [11, 18, 24, 50, 64],
        [8, 30, 41, 45, 66],
        [18, 24, 38, 55, 63]
        # [8, 24, 37, 54, 15, 65],
        # [63, 67, 47, 28, 18, 36],
        # [33, 20, 67, 62, 18, 55],
        # [4, 16, 20, 39, 47, 56]
              ]

pick_method = [None, "Algorithm", "App Quickpick", "Manual Picks"]

bet_amounts = [
               1.00, 1.00, 1.00, 1.00, 1.00, 1.00,
               1.00, 1.00, 1.00, 1.00, 1.00, 1.00
             # , 1.00
               ]

theory_used = 'Repeated/5 Non Drawn Numbers'

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

