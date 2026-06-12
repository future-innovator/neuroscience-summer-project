import pandas as pd

df = pd.DataFrame({"Name" : ["Alice", "Bob", "Charlie"], "Age" : [20, 22, 19]})

print(df)

#Only prints ages
print(df["Age"])

