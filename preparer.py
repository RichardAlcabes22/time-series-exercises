import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def convert_dates(df):
    '''
    takes in a string object in tsa_item dataset and converts in to date (no time) format
    
    '''
    df.sale_date = pd.to_datetime(df.sale_date.str.replace(' 00:00:00 GMT', ''))

def convert_date_opsd(df):
    '''
    takes in a string object in opsd dataset and converts to date (no time) format
    
    '''
    df['Date'] = pd.to_datetime(df['Date'])

def get_hist(df):
    ''' Gets histographs of acquired continuous variables'''

    # List of columns
    cols = [col for col in df.columns if df[col].dtype != 'O']

    for col in cols:
        plt.hist(df[col], edgecolor='black')
        plt.title(f'Distribution of {col}:')
        plt.show()


def plot_continuous_col(df):
    '''
    takes in tsa_item dataframe and plots histogrm for sale_amount and item_price continuous values
    
    '''
    cont_col = [df.sale_amount,df.item_price]
    for col in df.cont_col:
        plt.hist(df[col], edgecolor='black')
        plt.title(f'Distribution of {col}:')
        plt.show()




def index_date_opsd(df):
    df = df.set_index('Date').sort_index()
    return df

def date_to_index(df):
    '''
    takes in a dataframe and returns a dataframe that is reindexed and sorted (asc) by sale_date
    
    '''
    df = df.groupby('sale_date').sale_amount.sum().reset_index()
    return df

def date_info_cols(df):
    '''
    takes in the tsa datframe and creates 2 additional date info cols: month(numerical) and DAY_of_WEEK(numerical)
    '''
    df['month'] = df.sale_date.dt.month
    df['day_of_week'] = df.sale_date.dt.day_of_week
    return df


def create_sales_total(df):
    '''
    takes in the tsa datframe and creates an additional sales col: sales_total = sale_amount * item_price
    '''
    df['sales_total'] = df['sale_amount'] * df['item_price']

def date_info_cols_opsd(df):
    '''
    takes in the opsd datframe and creates 2 additional date info cols: month(numerical) and DAY_of_WEEK(numerical)
    '''
    df['month'] = df['Date'].dt.month
    df['day_of_week'] = df['Date'].dt.day_of_week
    return df

def fill_nan(df):
    '''
    fills in all NaNs with 0
    '''
    df.fillna(0,inplace=True)
    return df