# voobeeld om excel file te openen
import pandas as pd

df = pd.read_excel (r'C:\Users\ruben\Documents\test-greenhouse-data.xlsx') #(use "r" before the path string to address special character, such as '\'). Don't forget to put the file name at the end of the path + '.xlsx'
print (df)
