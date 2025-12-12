import pandas as pd 
import re

# load data file
data = pd.read_csv("fake_job_postings.csv")
print(data.head())

#Data Cleaning

data = data[['description', 'fraudulent']]

data = data.dropna(subset = ['description'])

data = data.reset_index(drop = True) # - reset index

print(f"number of sample data after cleaning {len(data)}")
print(data.head())

def clean_text(text):
    
    text = text.lower
    text = re.sub(r'<.*>', ' ', text)
    text = re.sub(r'[^a-z\s]]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()

data['clean description'] = data['description'].apply(clean_text)


