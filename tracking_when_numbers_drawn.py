
## Create a csv file that tracks when the numbers in that can be drawn have been
def numbers_drawn_csv(url, keno_nums, col_date, col_nums):
    import numpy as np
    import pandas as pd
    from lottery_analysis import list_conversion

    df = pd.read_csv(url,
                     index_col=0
                     )
    draw_dates = df[col_date].values

    d = pd.DataFrame(np.zeros((len(keno_nums) + 1, len(draw_dates))))

    d.columns = draw_dates

    for c in range(len(df)):
        num_list = list_conversion(df.iloc[c][col_nums])
        for num in num_list:
            d.iloc[num, c] = 1

    ## Save the dataframe as a csv
    d.to_csv('C:/Users/pstan/Documents/Continuing Education Data/lottery_tracking_dashboard/data/lottery_num_tracking.csv',
             lineterminator='\n',
             index=True,
             encoding='utf-8'
    )








