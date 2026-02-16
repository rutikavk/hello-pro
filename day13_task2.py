import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = {
    "SquareFootage": [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500, 3000, 3500],
    "Price": [40000, 50000, 60000, 75000, 90000, 110000, 130000, 160000, 200000, 250000],
    "Location": ["Urban", "Urban", "Suburban", "Suburban", "Urban",
                 "Rural", "Suburban", "Urban", "Rural", "Urban"]
}
df = pd.DataFrame(data)
plt.figure()
sns.scatterplot(x="SquareFootage", y="Price", data=df)
plt.title("Square Footage vs Price")
plt.show()
plt.figure()
sns.boxplot(x="Location", y="Price", data=df)
plt.title("Price Distribution by Location")
plt.show()
