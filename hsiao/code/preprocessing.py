import pandas as pd
import numpy as np


class Prep:
    def __init__(self, data_dir):
        self.pd = pd.read_csv(data_dir, index_col=0)
        self.x = self.pd.iloc[:, 1:]
        self.y = self.pd.iloc[:, 0] 

    def xy(self):
        return self.x, self.y

    def info(self):
        print("Dataframe of x\n", self.x, "\nDataframe of y\n", self.y)
        print("sum of null number of x\n", self.x.isnull().sum(), "\nsum of null number of y\n", self.y.isnull().sum())

    def drop_null(self, col_names):
        self.x = x.drop(col_names, axis=1)
        return x
    
    def label_en(self):
        pass

    def corr(self, y_col):
        return self.pd.corr()[y_col].sort_values()
        

