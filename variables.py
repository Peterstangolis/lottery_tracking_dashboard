played_lottery = True

url_lottery_guru = 'https://lotteryguru.com/ontario-lottery-results'

keno_logo_link = 'https://lotteryguru.com/pict/96850/ca-keno-2x-png'

data_url = 'https://github.com/Peterstangolis/lottery_tracking_dashboard/blob/main/data/keno_lottery_stats.csv?raw=true'

data_analysis_url =  'https://github.com/Peterstangolis/lottery_tracking_dashboard/blob/main/data/keno_lottery_analysis.csv?raw=true'

lott_analysis_csv = 'C:/Users/pstan/Documents/Continuing Education Data/lottery_tracking_dashboard/data/keno_lottery_analysis.csv'
lott_stats_csv = 'C:/Users/pstan/Documents/Continuing Education Data/lottery_tracking_dashboard/data/keno_lottery_stats.csv'


my_numbers = [
    [4, 18, 28, 35, 50],
    [18, 32, 34, 43, 56],
    [17, 34, 36, 50, 64],
    [3, 18, 32, 43, 64],
    [18, 28, 39, 50, 56],
    [4, 17, 32, 56, 64],
    [4, 21, 28, 32, 43, 56],
    [18, 32, 34, 50, 64],
    [3, 21, 28, 50, 56],
    [3, 17, 36, 56, 64],
    [18, 32, 36, 50, 56],
    [28, 36, 50, 56, 64]
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

theory_used = 'Not Repeated 1 Game'

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

