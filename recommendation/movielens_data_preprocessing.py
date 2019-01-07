import numpy as np
import pandas as pd


def get_data():
    df_ratings = pd.read_csv('./data/ml-1m/ratings.dat', 
        names=['uid', 'movie_id', 'rate', 'timestamp'], sep='::')
    print('df_ratings.shape is ', df_ratings.shape)
    print('df_ratings.head is ', df_ratings.head(10))


get_data()

