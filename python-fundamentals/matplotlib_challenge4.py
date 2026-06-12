import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({"Brain Region" : ["Hippocampus", "Amygdala", "Cortex"], "Activity" : [80, 65, 95]})

plt.bar(df["Brain Region"], df["Activity"])

plt.title("Activity by Brain Region")
plt.xlabel("Brain Region")
plt.ylabel("Activity")

plt.tight_layout()

plt.show()
