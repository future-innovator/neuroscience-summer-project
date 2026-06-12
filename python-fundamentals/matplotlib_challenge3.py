import matplotlib.pyplot as plt

regions = ["Hippocampus", "Amygdala", "Cortex"]
activity = [80, 65, 95]

plt.bar(regions, activity)

plt.title("Activity by Brain Region")
plt.xlabel("Brain Region")
plt.ylabel("Activity")

plt.tight_layout()

plt.show()
