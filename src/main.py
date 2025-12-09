import pandas as pd 
# load data file
data = pd.read_csv("fake_job_postings.csv")
print(data.head())

#Data Cleaning

data = data[['description', 'fraudulent']]

data = data.dropna(subset = ['description'])

data = data.reset_index(drop = True) # - reset index

print(f"number of sample data after cleaning {len(data)}")
print(data.head())