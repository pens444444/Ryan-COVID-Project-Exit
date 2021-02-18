import pandas as pd
## suppose file1_df and file2_df are related Dataframe object for file1 and file2 respectively.
df1=pd.read_csv('us-covid-19-total-people-vaccinated.csv')
df2=pd.read_csv('us-covid-number-fully-vaccinated.csv')
df3=pd.read_csv('us-covid-19-share-people-vaccinated.csv')
merged_df1 = pd.merge(df1, df2, how='left', on=['Entity','Code','Date'])
merged_df=pd.merge(merged_df1, df3, how='left', on=['Entity','Code','Date'])
merged_df['full_percentage']=merged_df['people_fully_vaccinated']/merged_df['people_vaccinated']*100
merged_df.to_csv('Vaccination Percentage.csv', index=False)