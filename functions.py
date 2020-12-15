def get_datetimes(df): 
    """Takes in a dataframe 
    Returns datetime formated column""" 
    import pandas as pd
    return pd.to_datetime(df.columns.values[1:], format='%Y-%m') 




def melt_data(df): 
    """Takes in a dataframe wide format
    Returns a dataframe long format""" 
    import pandas as pd
    melted = pd.melt(df, var_name='time')
    melted['time'] = pd.to_datetime(melted['time'], infer_datetime_format=True)
    melted = melted.dropna(subset=['value'])
    return melted.set_index('time')