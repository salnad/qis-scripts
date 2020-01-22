import fundamentals
import argparse
import sys
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--tickers", help="list of tickers, comma seperated")
parser.add_argument("-f", "--filename", help="name of csv file to save to (make sure to add .csv)")
parser.add_argument("-ys", "--year_start", type=int, help="starting year")
parser.add_argument("-ye", "--year_end", type=int, help="ending year")

args = parser.parse_args()

def main():
    # if you want to write out commands instead of using the CLI, insert them in this function
    # start ->
    pass
    # <- end


if len(sys.argv) <= 1:
    main()
else:

    tickers = args.tickers.split(',')
    if args.filename:
        filename = args.filename
    else:
        filename = 'result.csv'
    year_start = args.year_start
    year_end = args.year_end
    list_of_df = []
    for ticker in tickers:
        ticker_data = fundamentals.get_fundamentals_data(ticker, year_start, year_end)
        first = ticker_data['Fiscal Period'].iloc[0] + ' ' + str(ticker_data['Fiscal Year'].iloc[0])
        last = ticker_data['Fiscal Period'].iloc[-1] + ' ' + str(ticker_data['Fiscal Year'].iloc[-1])
        print(f'added data for {ticker} from {first} to {last}')
        list_of_df.append(ticker_data)
    final_df = pd.concat(list_of_df)
    final_df.to_csv(filename)

'''

-t, --tickers, tickers (comma seperated)
-ys, --year_start, starting year
-ye, --year_end, ending year
-f, --filename, filename data is saved (ends with .csv)

default, run what's in main

'''