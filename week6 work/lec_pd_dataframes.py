'''
dataframe处理表格型数据
'''

""" lec_pd_dataframes.py

Companion codes for the lecture on Dataframes
"""

import pandas as pd


# ---------------------------------------------------------------------------- 
#   The dates and prices lists
# ---------------------------------------------------------------------------- 
dates = [
  '2020-01-02', 
  '2020-01-03',
  '2020-01-06',
  '2020-01-07',
  '2020-01-08',
  '2020-01-09',
  '2020-01-10',
  '2020-01-13',
  '2020-01-14',
  '2020-01-15',
  ]

prices = [
  7.1600, 
  7.1900,
  7.0000,
  7.1000,
  6.8600,
  6.9500,
  7.0000,
  7.0200,
  7.1100,
  7.0400,
  ]

# Business (trading) day counter
bday = [
  1,
  2,
  3,
  4,
  5,
  6,
  7,
  8,
  9,
  10]

# ---------------------------------------------------------------------------- 
#   Create two series
# ---------------------------------------------------------------------------- 

# Series with prices
prc_ser = pd.Series(data=prices, index=dates)
# print(prc_ser)

# Series with trading day
bday_ser = pd.Series(data=bday, index=dates)
# print(bday_ser)


# 1. 创建dataframe
# ---------------------------------------------------------------------------- 
#   Create a dataframe
# ---------------------------------------------------------------------------- 
# Data Frame with close and Bday columns
# 会以两个series的index为key合并两个series，共享index
df = pd.DataFrame({'Close': prc_ser, 'bday': bday_ser})# {'列的名称':series}
# print(df)

# 2. df的检索
# ---------------------------------------------------------------------------- 
#   Accessing the indexes in a dataframe
# ---------------------------------------------------------------------------- 
# The attribute `columns` returns the column index
# 找到所有columns的名称
# print(df.columns)
# print('The type of this column is', type(df.columns))


# We can get the series corresponding to a column index label
# col0 = df['Close']
# print(col0)

# col1 = df['bday']
# print(col1)

# Just like any series, you can access the index using:
# print(col0.index)
# print(type(col0.index))

# In fact, this corresponds to the Dataframe index as well
# print(df.index)
# print(type(df.index))


# 2，修改
# ----------------------------------------------------------------------------
#   Modifying columns and indexes
# ----------------------------------------------------------------------------
# Modify columns and indexes
# df.columns = ['A', 'B']
# df.index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(df)

# Then revert back
# df.columns = ['Close', 'Bday']
# df.index = [
#  '2020-01-02',
#  '2020-01-03',
#  '2020-01-06',
#  '2020-01-07',
#  '2020-01-08',
#  '2020-01-09',
#  '2020-01-10',
#  '2020-01-13',
#  '2020-01-14',
#  '2020-01-15',
# ]
# print(df)


# 3. df排序
# ----------------------------------------------------------------------------
#   Sorting 
# ----------------------------------------------------------------------------

# Create a series with an unsorted index 
new_ser = pd.Series(data=[1, 3, 2], index=['a', 'c', 'b'])
# print(new_ser)

# This will return 'False'
#print(new_ser.is_monotonic_increasing) 

# Sort the series based on the index
# 不会改变原有的index，但会产出一个新的index序列
# sorted_ser = new_ser.sort_index()
# print(sorted_ser)
# print(new_ser)

# This will return only the first rows (not the entire series as before)
#x = sorted_ser['a':'b'] # --> only first two rows 
#print(x) 
# Out:
# a    1
# b    2
# dtype: int64

# `sorted_ser` is sorted so the following will return the intersection between
# the slice and the row labels
#x = sorted_ser['b':'z'] 
#print(x) 
# Out:
# b    2
# c    3
# dtype: int64

# 无需产出新的index，在原有数据上修改：inplace=True
# Create a series with an unsorted index 
ser_sort_inplace = pd.Series(data=[1,3,2], index=['a', 'c', 'b'])

# Sort the series. Note that we are not assigning this function call
# to a new variable.
ser_sort_inplace.sort_index(inplace=True)
print(ser_sort_inplace)


