#%%
import pandas as pd
from utils import import_excel_file_as_pd_df
file_path='files/130moscu.xlsx'
df = import_excel_file_as_pd_df(file_path)
print(df.head())
#%% 