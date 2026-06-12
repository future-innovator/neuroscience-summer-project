import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

plt.plot(x, y)

plt.title("Week vs Total Hours Studied")
plt.xlabel("Week")
plt.ylabel("Total Hours Studied")

plt.tight_layout()

plt.show()
