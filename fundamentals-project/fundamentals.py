import requests
import pandas as pd
import math

# here, paste the api key for SimFin
api_key = "b8vabmV9ZlSP7TCmUYewGrRJAyS8Jc8V"

# REQUIRES: ticker name (eg. APPL), starting year and ending year (eg. 2011 and 2017)
# EFFECTS: returns a dataframe, which contains the fundamentals data seen on README.md for each quarter in [years_start, years_end] range
def get_fundamentals_data(ticker, year_start, year_end):
    all_data_df = pd.read_pickle('all-data.pkl')
    years = [x for x in range(year_start, year_end+1)]
    result_df = all_data_df[(all_data_df['Fiscal Year'].isin(years)) & (all_data_df['Ticker'] == ticker)]
    return result_df