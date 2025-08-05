import numpy as np
import pandas as pd

categories = ['a','b','c']
my_list = [-1,-2,-3]
arr = np.array([100,99,98])

my_series = pd.Series(data=my_list)

print(my_series)

df = pd.DataFrame(my_list)

print(df)