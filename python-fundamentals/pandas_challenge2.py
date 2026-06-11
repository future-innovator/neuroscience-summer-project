import pandas as pd

df = pd.DataFrame({
    "Name" : ["Alice", "Bob", "Charlie"], 
    "Age" : [20, 22, 19]
    })

print(df.columns)

print(df.shape)
