played_lottery = True

url_lottery_guru = 'https://lotteryguru.com/ontario-lottery-results'

keno_logo_link = 'https://lotteryguru.com/pict/96850/ca-keno-2x-png'

data_url = 'https://github.com/Peterstangolis/lottery_tracking_dashboard/blob/main/data/keno_lottery_stats.csv?raw=true'

data_analysis_url =  'https://github.com/Peterstangolis/lottery_tracking_dashboard/blob/main/data/keno_lottery_analysis.csv?raw=true'

lott_analysis_csv = 'C:/Users/pstan/Documents/Continuing Education Data/lottery_tracking_dashboard/data/keno_lottery_analysis.csv'
lott_stats_csv = 'C:/Users/pstan/Documents/Continuing Education Data/lottery_tracking_dashboard/data/keno_lottery_stats.csv'


my_numbers = [
    [4, 18, 37, 42, 53],
    [18, 25, 34, 42, 57],
    [10, 38, 41, 59, 62],
    [9, 10, 38, 53, 68],
    [16, 24, 32, 59, 64],
    [5, 10, 26, 34, 57],
    [10, 25, 42, 50, 69],
    [9, 18, 42, 59, 62],
    [4, 25, 34, 57, 64],
    [16, 32, 42, 57, 69],
    [4, 10, 36, 59, 69],
    [7, 19, 40, 58, 69],
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

theory_used = 'Not Repeated 1 Game & groupings'

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

numbers_breakdown = {
    "ODD_1_19" : [1, 3, 5, 7, 9, 11, 13, 15, 17, 19],
    "EVEN_2_18" : [2, 4, 6, 8, 10, 12, 14, 16, 18],
    "ODD_21_35" : [21, 23, 25, 27, 29, 31, 33, 35],
    "EVEN_20_34" : [20, 22, 24, 26, 28, 30, 32, 34],
    "ODD_37_51" : [37, 39, 41, 43, 45, 47, 49, 51],
    "EVEN_36_52" : [36, 38, 40, 42, 44, 46, 48, 50, 52],
    "ODD_53_69" : [53, 55, 57, 59, 61, 63, 65, 67, 69],
    "EVEN_54_70" : [54, 56, 58, 60, 62, 64, 66, 68, 70]
}

