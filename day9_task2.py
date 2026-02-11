import pandas as pd
grades=pd.Series([85,None,92,45,None,78,55])
print("original:\n",grades)
print(grades.isnull())
print("The filled series:\n",grades.fillna(0))
marks=grades[grades>60]
print("The filtered results:\n",marks)
