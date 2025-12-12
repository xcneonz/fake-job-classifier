import pandas as pd
import re

#Load data
data = pd.read_csv("fake_job_postings.csv")
data = data[['description', 'fraudulent']].dropna()

data = data.reset_index(drop = True)

def clean_text(text):
    text = text.lower()
    text = re.sub(r'<.*?>', ' ', text)
    text = re.sub(r'[^a-z\s+]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

data['clean_description'] = data['description'].apply(clean_text)

#save the cleaned csv
data.to_csv('cleaned_fake_posting.csv', index = False)
