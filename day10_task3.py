import pandas as pd
data={
"Location":[" New York","new york", "NEW YORK"]}
df=pd.DataFrame(data)
print("Before Cleaning:")
print(df["Location"].unique())
df["Location"]=df["Location"].str.strip()
df["Location"]=df["Location"].str.lower()
print("After cleaning:")
print(df["Location"].unique())