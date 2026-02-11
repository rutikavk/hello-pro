import pandas as pd
usernames=pd.Series(['Alice','boB','Charlie_Data','daisy'])
print(usernames.str.strip())
print(usernames.str.lower())
print(usernames.str.contains('a'))