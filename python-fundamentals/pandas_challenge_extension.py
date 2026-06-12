import pandas as pd

df = pd.DataFrame({"Name" : ["Alice", "Bob", "Charlie"], "Age" : [20, 22, 19]})

# Boolean indexing:
# Keep only rows where Age is greater than 20
print(df[df["Age"] > 20])
