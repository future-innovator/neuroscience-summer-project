import pandas as pd

df = pd.DataFrame({"Name" : ["Alice", "Bob", "Charlie"], "Age" : [20, 22, 19]})

print(df)

ages = df["Age"]
print(ages)

# A Pandas Series supports methods like mean(), max(), and min() because it represents a sequence of values, similarly to a NumPy array. Pandas is built on top of NumPy, so many of NumPy's operations are available on Pandas' Series Objects
print(f"Mean age is {ages.mean()}")
print(f"Maximum age is {ages.max()}")
print(f"Minimum age is {ages.min()}")
