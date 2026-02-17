# Import libraries
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Step 1: Create sample dataset
df = pd.DataFrame({
    'Transmission': ['Automatic', 'Manual', 'Automatic', 'Manual'],
    'Color': ['Red', 'Blue', 'Green', 'Red']
})

print("Original Data:")
print(df)

# Step 2: Apply Label Encoding to Transmission
le = LabelEncoder()
df['Transmission'] = le.fit_transform(df['Transmission'])

# Step 3: Apply One-Hot Encoding to Color with drop_first=True
df = pd.get_dummies(df, columns=['Color'], drop_first=True,dtype=int)

print("\nEncoded Data:")
print(df)
