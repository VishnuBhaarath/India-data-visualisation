import pandas as pd 

import matplotlib.pyplot as plt 


data = pd.read_csv("train.csv")

print(data.describe())