def build_csv(keywords, filename):
    """
    Searches for all items in keywords

    :param keywords: a list of keywords
    :param filename: the filename of the csv file
    """
    from pytrends.request import TrendReq
    # Login to Google
    pytrend = TrendReq()

    # These are the keywords
    pytrend.build_payload(kw_list=keywords)

    # Creates interest_over_time dataframe
    interest_over_time_df = pytrend.interest_over_time()
    print(interest_over_time_df.info())
    # Builds csv with filename "filename"
    interest_over_time_df.to_csv(filename, sep='\t')

build_csv(['bitcoin'], 'bitcoin')